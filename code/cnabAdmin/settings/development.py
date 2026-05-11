from .settings import *


SECRET_KEY = 'django-insecure-ym=%tc_4@8&c31auxstdt$5jh^v+5ir7d+&jpp%2u651ci7@qc'

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'development_db.sqlite3',
    }
}