# API для Yatube

REST API для социальной сети Yatube: публикации, комментарии,
сообщества, подписки и JWT-аутентификация.

## Стек

- Python 3.12
- Django 6
- Django REST Framework
- Djoser + SimpleJWT
- SQLite

## Установка

```bash
python -m venv venv
venv/Scripts/activate   
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver