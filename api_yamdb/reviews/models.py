from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import UniqueConstraint

from users.models import User
from reviews.validators import year_validator


class Category(models.Model):
    """Модель для категорий."""

    name = models.CharField(verbose_name='Название группы',
                            max_length=200)
    slug = models.SlugField(verbose_name='Уникальный URL фрагмент',
                            max_length=50,
                            unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    """Модель для жанров."""

    name = models.CharField(verbose_name='Название жанра',
                            max_length=200)
    slug = models.SlugField(verbose_name='Уникальный URL фрагмент',
                            max_length=50,
                            unique=True)

    def __str__(self):
        return self.name


class Title(models.Model):
    """Модель для произведений."""

    name = models.CharField(verbose_name='Название',
                            max_length=200)
    year = models.IntegerField(verbose_name='Дата выхода',
                               validators=(year_validator,))
    genre = models.ManyToManyField(Genre,
                                   verbose_name='Жанр',
                                   through='GenreTitle')
    category = models.ForeignKey(Category,
                                 verbose_name='Категория',
                                 on_delete=models.SET_NULL,
                                 related_name='titles',
                                 null=True)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    """Связующая модель для жанров-произведений."""

    title = models.ForeignKey(Title,
                              verbose_name='Произведение',
                              on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre,
                              verbose_name='Жанр',
                              on_delete=models.CASCADE)


class Review(models.Model):
    """Класс для отзывов."""

    text = models.TextField()
    title = models.ForeignKey(Title,
                              related_name='reviews',
                              on_delete=models.CASCADE)
    author = models.ForeignKey(User,
                               related_name='reviews',
                               on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(validators=[MinValueValidator(1),
                                            MaxValueValidator(10)])
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        constraints = [UniqueConstraint(fields=['author', 'title'],
                                        name='unique_review')]

    def __str__(self):
        return self.text


class Comment(models.Model):
    """Класс для комментариев."""

    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,
                               related_name='comments',
                               on_delete=models.CASCADE)
    review = models.ForeignKey(Review,
                               related_name='comments',
                               on_delete=models.CASCADE)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.text
