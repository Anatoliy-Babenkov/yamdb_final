![yamdb Workflow Status](https://github.com/Anatoliy-Babenkov/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
```
#Проект 𝕐𝕒𝕄𝔻𝕓
```
Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха. Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»). 
Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). 
Добавлять произведения, категории и жанры может только администратор.
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.
Пользователи могут оставлять комментарии к отзывам.
Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи.
```
### По адресу http://127.0.0.1:8000/redoc/ к нему подключена документация будущего API.
```
Как запустить проект на тестовом сервере:
```
Клонировать репозиторий, перейти в директорию с проектом.
```
Cоздать и активировать виртуальное окружение:
```
python -m venv venv
```
Выполнить миграции:
```
python manage.py migrate
```
Запустить проект:
```
Авторы:
```
Цуккер Сергей  
Варламов Антон  
Бабенков Анатолий  
