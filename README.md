# my_site



Мой сайт, блог.
Посты можно разбить по категориям, любой желающий может оставить комментарий без регистрации.  


Что неплохо было бы сделать:  
Часть функционала, касающаяся бота, еще в процессе написания.  
Если будет хотя бы пару десятков постов - прикурчу пагинацию.  

####  Стек:  

Python 3.8  
Django 4.2  
Aiogram 2  
SQLite  
Python-dotenv  
Bulma  

####  Запуск

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:rdg0/my_site.git  
cd my_site
```

Cоздать и активировать виртуальное окружение:  

```
python3 -m venv env  
source env/bin/activate  
python3 -m pip install --upgrade pip  
```

Установить зависимости из файла requirements.txt:  
```
pip install -r requirements.txt  
```

Перейти в директорию с manage.py:  

```
cd rdg0_site
```

Выполнить миграции:  
```
python3 manage.py makemigrations  
python3 manage.py migrate  
```

Подготовить статику:  
```
python3 manage.py collectstatic
```

Создать суперюзера:  
```
python3 manage.py createsuperuser
```

В rdg0_site/settings.py создать .env файл c добавив DJANGO_SECRET_KEY=... для последующего импорта в settings.py.  


Запустить проект:  
```
python3 manage.py runserver
```
