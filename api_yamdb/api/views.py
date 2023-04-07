from api.auth import send_confirmation_code
from api.filters import TitleFilter
from api.mixins import ListCreateDestroyViewSet
from api.permissions import IsAdmin, IsAdminOrReadOnly, IsAuthorOrReadOnly
from api.serializers import (
    GetJWTTokenSerializer, SignUpSerializer, UserRestrictedSerializer,
    UserSerializer, ReviewSerializer, CommentSerializer, CategorySerializer,
    GenreSerializer, TitleSerializer, TitleSerializerList
)
from django.contrib.auth.tokens import default_token_generator
from django.db import IntegrityError
from django.db.models import Avg
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from reviews.models import Category, Genre, Review, Title
from users.models import User


class CategoryViewSet(ListCreateDestroyViewSet):
    """Вьюсет для категорий.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GenreViewSet(ListCreateDestroyViewSet):
    """Вьюсет для жанров.
    """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class TitleViewSet(viewsets.ModelViewSet):
    """Вьюсет для произведений.
    """
    queryset = Title.objects.annotate(rating=Avg('reviews__score'))
    serializer_class = TitleSerializer
    permission_classes = (IsAdminOrReadOnly, )
    ordering_fields = ('name', )
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return TitleSerializerList
        return TitleSerializer


class SignUpView(APIView):
    """Запрос регистрации нового пользователя. Создание нового пользователя,
    отправка confirmation code для подтверждения регистрации.
    """

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        email = serializer.validated_data.get('email')
        try:
            user, _ = User.objects.get_or_create(
                username=username,
                email=email
            )
        except IntegrityError as error:
            raise ValidationError(
                ('Ошибка создания новой записи '
                 f'username: {username}, email: {email}')
            ) from error
        token = default_token_generator.make_token(user)
        user.save()
        send_confirmation_code(user, token)
        return Response(serializer.validated_data, status=HTTP_200_OK)


@method_decorator(csrf_exempt, name='dispatch')
class GetJWTTokenView(APIView):
    """
    Запрос на получение JWT токена.
    Для получения требуется confirmation code.
    """

    def post(self, request, token=None):
        serializer = GetJWTTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        user = get_object_or_404(User, username=username)
        if not default_token_generator.check_token(user, token):
            return Response(
                {
                    "Неверный код доступа "
                },
                status=HTTP_400_BAD_REQUEST
            )
        return Response(
            {
                "token": str(
                    RefreshToken.for_user(user).access_token
                )
            }
        )


class UserViewSet(ModelViewSet):
    """Пользователь может просматривать и редактировать данные своей учётной
    записи.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdmin, )
    lookup_field = 'username'
    filter_backends = (SearchFilter, )
    search_fields = ('username', )
    http_method_names = ('get', 'post', 'patch', 'delete')

    @action(methods=('get', 'patch'),
            detail=False,
            url_path='me',
            url_name='self_account',
            permission_classes=[IsAuthenticated, ])
    def self_account(self, request):
        """Просмотр и изменение своей учётной записи."""
        if request.method == 'PATCH':
            serializer = UserRestrictedSerializer(request.user,
                                                  data=request.data,
                                                  partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
        serializer = UserRestrictedSerializer(request.user)
        return Response(serializer.data, status=HTTP_200_OK)


class ReviewViewSet(viewsets.ModelViewSet):
    """Вьюсет для отзывов.
    """
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthorOrReadOnly, )

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для комментариев.
    """
    permission_classes = (IsAuthorOrReadOnly, )
    serializer_class = CommentSerializer

    def get_queryset(self):
        review = get_object_or_404(Review, id=self.kwargs.get('review_id'))
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(Review, id=self.kwargs.get('review_id'))
        serializer.save(review=review, author=self.request.user)
