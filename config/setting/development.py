from config.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
SECRET_KEY = 'django-insecure-4&b@r)8h_o(^3gk*khk&%_eu=_!^t$yrfg_gmp6fh7hsv%-r@w'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home.apps.HomeConfig',
    'accounts.apps.AccountsConfig',
]
  
STATIC_ROOT=BASE_DIR/'/static'
MEDIA_ROOT=BASE_DIR/'media'

STATICFILES_DIRS=[
    BASE_DIR/'static',
    BASE_DIR/'media',
]