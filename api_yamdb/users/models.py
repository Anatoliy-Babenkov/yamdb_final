from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from django.db.models import CharField, EmailField, TextField

from .validators import username_validation


class User(AbstractUser):
    """Аутентифицированный пользователь - может читать всё,
    как и Аноним, может публиковать отзывы и ставить оценки произведениям
    (фильмам/книгам/песенкам), может комментировать отзывы; может
    редактировать и удалять свои отзывы и комментарии, редактировать
    свои оценки произведений. Эта роль присваивается по умолчанию каждому
    новому пользователю.
    """
    ROLE_ADMIN = 'admin'
    ROLE_MODERATOR = 'moderator'
    ROLE_USER = 'user'
    role_choice = ((ROLE_ADMIN, 'admin'),
                   (ROLE_MODERATOR, 'moderator'),
                   (ROLE_USER, 'user'))
    username = CharField(max_length=150,
                         unique=True,
                         validators=(username_validation,),
                         verbose_name='Имя пользователя',
                         help_text='Имя пользователя')
    email = EmailField(max_length=254,
                       unique=True,
                       verbose_name='Адрес электронной почты',
                       help_text='Адрес электронной почты',
                       validators=(EmailValidator(
                           message='Некорректный email'), ))
    first_name = CharField(max_length=150,
                           blank=True,
                           verbose_name='Имя',
                           help_text='Имя',
                           null=True)
    last_name = CharField(max_length=150,
                          blank=True,
                          verbose_name='Фамилия',
                          help_text='Фамилия',
                          null=True)
    bio = TextField(blank=True,
                    verbose_name='Биография',
                    help_text='Биография',
                    null=True)
    role = CharField(max_length=15,
                     choices=role_choice,
                     default=ROLE_USER,
                     verbose_name='Роль пользователя',
                     help_text='Роль пользователя')
    password = None
    last_login = None
    date_joined = None

    @property
    def is_admin(self):
        """Администратор - полные права на управление всем контентом проекта.
        Может создавать и удалять произведения, категории и жанры.
        Может назначать роли пользователям."""
        return (self.role == User.ROLE_ADMIN
                or self.is_staff
                or self.is_superuser)

    @property
    def is_moderator(self):
        """Модератор - те же права, что и у Аутентифицированного
        пользователя, плюс право удалять и редактировать любые
        отзывы и комментарии"""
        return self.role == User.ROLE_MODERATOR
