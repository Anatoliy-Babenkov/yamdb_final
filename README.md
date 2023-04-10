![yamdb Workflow Status](https://github.com/Anatoliy-Babenkov/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

<h1><p align="center"> 𝕐𝕒𝕄𝔻𝕓 ℙ𝕣𝕠𝕛𝕖𝕔𝕥 </p></h1>

<h2><p align="center"> Описание проекта: </p></h2>

<b>П</b>роект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха. Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).
<br>
<b>П</b>роизведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). Добавлять произведения, категории и жанры может 
только администратор.
<br>
<b>Б</b>лагодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.
Пользователи могут оставлять комментарии к отзывам. Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи.
<h2><p align="center"></p></h2>

<h2><p align="center">Как запустить проект:</p></h2>

<b>1.</b> Скопировать репозиторий:
```
git clone git@github.com:Anatoliy-Babenkov/yamdb_final.git
```
<b>2.</b> Cоздать и активировать виртуальное окружение:
* <i>Linux</i>:
```
  source venv/bin/activate
```
* <i>Windows</i>:
```
  source venv/Scripts/activate
```
<b>3.</b> Обновить <i>PIP</i>:
```
python -m pip install --upgrade pip
```
<b>4.</b> Установить зависимости из <i>requirements.txt</i>:
```
pip install -r api_yamdb/requirements.txt
```
<b>Необходимо установить:</b>
* <a href=https://www.docker.com/get-started>Docker</a>
* <a href=https://docs.docker.com/compose/install/>Docker-compose</a>

<b>5.</b> Из папки проекта <i>Infra</i> ввести команду:
```
docker-compose up --build
```
<b>6.</b> Узнать id контейнера:
```
docker container ls
```
<b>7.</b> Зайти в контейнер <i>web</i>:
```
docker exec -it <CONTAINER ID> sh
```
<b>8.</b> Провести миграцию базы данных:
```
python manage.py migrate
```
<b>9.</b> Провести сбор статики:
```
python manage.py collectstatic
```
<h2><p align="center"></p></h2>

<h2><p align="center">После запуска, подробная информация о использовании:</p></h2>
<p align="center"><a href=http://0.0.0.0/redoc/>Redoc</a></p>
<h2><p align="center"></p></h2>

<h2><p align="center">При использовании <i>Github: Actions</i>:</p></h2>
Необходимо создать Secrets со следующими данными:

<br>
<br>

* <b>DB_ENGINE</b>: Двигатель адаптера базы данных (django.db.backends.postgresql);
* <b>DB_HOST</b>: Хост базы данных (db);
* <b>DB_NAME</b>: Название базы данных (postgres);
* <b>DB_PORT</b>: Порт для базы данных (5432);
* <b>DOCKER_PASSWORD</b>: Пароль пользователя Docker;
* <b>DOCKER_USERNAME</b>: Пользователь Docker;
* <b>HOST</b>: Адрес сервера для запуска проекта;
* <b>POSTGRES_PASSWORD</b>: Пароль пользователя базы данных (postgres);
* <b>POSTGRES_USER</b>: Пользователь базы данных (postgres);
* <b>SSH_KEY</b>: Ключ для входа на сервер запуска проекта;
* <b>TELEGRAM_TO</b>: ID Telegram куда следует направить отчёт об успешном запуске;
* <b>TELEGRAM_TOKEN</b>: ID Telegram бота длч отправки;
* <b>USER</b>: Пользователь для входа на сервер запуска проекта;

<h2><p align="center"></p></h2>

<h2><p align="center">Авторы кода <i>api_yamdb</i>:</p></h2>

<br>
<br>

<p align="center">Цуккер Сергей</p>  
<p align="center">Варламов Антон</p>  
<p align="center"><a href=https://github.com/Anatoliy-Babenkov>Бабенков Анатолий</a></p>
<br>
<br>

<h2><p align="center"></p></h2>

<h2><p align="center">CI и CD проекта <i>api_yamdb</i>:</p></h2>

<br>
<br>

<p align="center"><a href=https://github.com/Anatoliy-Babenkov>Бабенков Анатолий</a></p>

<p color=Red>Ya</p>.Практикум