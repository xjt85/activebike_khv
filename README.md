# ACTIVEBIKE_KHV
## Сайт велосипедного сообщества города Хабаровска

### Технологии: Django, HTML5, CSS3, Leaflet.js, gpxpy, polyline.

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)

Сайт велосипедного сообщества города Хабаровска https://activebike-khv.ru

## Подготовка и запуск проекта
### Склонировать репозиторий на локальную машину:

```
git clone https://github.com/xjt85/activebike_khv
```

### Установите и активируйте виртуальное окружение:
```
python -m venv venv
source venv/scripts/activate
```

### Установите зависимости:
```
pip install -r requirements.txt
pip3 install pep8-naming flake8-broken-line flake8-return flake8-isort autopep8
```

* Cоздайте .env файл и впишите:
```
SECRET_KEY = ""
ALLOWED_HOSTS = ""
CSRF_TRUSTED_ORIGINS = ""
TLG_API_ID = ""
TLG_API_HASH = ""
TLG_USERNAME = ""
TLG_CHANNEL_URL = ""
TLG_SESSION_STRING = ""
```

* Примените миграции:
```
python manage.py migrate
```

* Создайте суперпользователя Django:
```
sudo docker-compose exec backend python manage.py createsuperuser
```

* Запустите сервер разработки:
```
python manage.py runserver
```

Проект доступен по [адресу](https://activebike-khv.ru).

### Автор: [Роман Чуклинов](https://t.me/xjavue).
