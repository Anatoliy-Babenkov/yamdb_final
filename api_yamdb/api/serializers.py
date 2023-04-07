from django.db import IntegrityError
from django.core.validators import validate_email
from rest_framework import serializers
from reviews.models import Category, Comment, Genre, Review, Title, User
from users.models import username_validation


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с отзывами.
    """
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)

    def create(self, validated_data):
        try:
            review = Review.objects.create(**validated_data)
        except IntegrityError:
            raise serializers.ValidationError(
                'Нельзя оставить больше одного обзора.'
            )
        return review

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date')


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для комментариев.
    """
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор модели User.
    """
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'bio', 'role')

    def validate_username(self, value):
        """Проверка имени пользователя.
        """
        return username_validation(value)


class SignUpSerializer(serializers.Serializer):
    """Сериализатор регистрации нового пользователя.
    """
    username = serializers.CharField(max_length=150,
                                     required=True,
                                     validators=[username_validation, ])
    email = serializers.EmailField(max_length=254,
                                   required=True,
                                   validators=[validate_email, ])


class UserRestrictedSerializer(UserSerializer):
    """Сериализатор модели User для изменения данных аккаунтов.
    """
    username = serializers.CharField(max_length=150,
                                     required=True,
                                     validators=[username_validation, ])
    email = serializers.EmailField(max_length=254,
                                   required=True,
                                   validators=[validate_email, ])

    class Meta(UserSerializer.Meta):
        read_only_fields = ('username', 'email', 'role')


class GetJWTTokenSerializer(serializers.Serializer):
    """Сериализатор запроса JWT токена.
    """
    username = serializers.CharField(max_length=150,
                                     required=True,
                                     validators=[username_validation])
    confirmation_code = serializers.CharField(max_length=5,
                                              required=True)


class CategorySerializer(serializers.ModelSerializer):
    """Серилизатор для категорий.
    """

    class Meta:
        model = Category
        fields = ('name', 'slug',)


class GenreSerializer(serializers.ModelSerializer):
    """Серилизатор для жанров.
    """

    class Meta:
        model = Genre
        fields = ('name', 'slug',)


class TitleSerializerList(serializers.ModelSerializer):
    """Серилизатор для произведений.
    """
    genre = GenreSerializer(many=True)
    category = CategorySerializer()
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'rating',
                  'description', 'genre', 'category')


class TitleSerializer(serializers.ModelSerializer):
    """Серилизатор для произведений.
    """
    genre = serializers.SlugRelatedField(many=True,
                                         queryset=Genre.objects.all(),
                                         slug_field='slug')
    category = serializers.SlugRelatedField(slug_field='slug',
                                            queryset=Category.objects.all())

    class Meta:
        model = Title
        fields = ('id', 'name', 'year',
                  'description', 'genre', 'category')
