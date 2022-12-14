"""
Django settings for newsproject project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'style': '{',
    # Формат
    'formatters': {
        'simple': {  # симпл мэс
            'format': '%(asctime)-8s %(levelname)-8s %(message)s'
            # время возникновения сообщения, уровень логирования, сообщение
        },
        'advanced_path': {  # WARNING
            'format': '%(asctime)-8s %(levelname)-8s %(pathname)-8s %(message)s'
            # время возникновения сообщения, уровень логирования, путь к источнику события, сообщение
        },
        'advanced_path_exc': {  # ERROR и CRITICAL
            'format': '%(asctime)-8s %(levelname)-8s %(pathname)-8s %(exc_info)-8s %(message)s'
            # время возникновения сообщения, уровень логирования, путь к источнику события, стэк ошибки, сообщение
        },
        'advanced_module': {  # general.log, уровень INFO
            'format': '%(asctime)-8s %(levelname)-8s %(module)-8s %(message)s'
            # время возникновения сообщения, уровень логирования, модуль в котором возникло сообщение, сообщение
        },
    },
    # Фильтры
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    # Хэндлеры
    'handlers': {
        'console_debug': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'console_warning': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'advanced_path'
        },
        'console_error': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'advanced_path_exc'
        },
        # general.log
        'file_general': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'formatter': 'advanced_module',
            'filename': 'general.log'
        },
        # errors.log
        'file_errors': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'advanced_path_exc',
            'filename': 'errors.log',
        },
        # security.log
        'file_security': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'advanced_module',
            'filename': 'security.log'
        },
        # Почта
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'advanced_path'
        },
    },
    # Регистраторы
    'loggers': {
        # django
        'django': {
            'handlers': ['console_debug', 'console_warning', 'console_error', 'file_general'],
            'level': 'DEBUG',
            'propagate': 'True',
        },
        # django.request
        'django.request': {
            'handlers': ['file_errors', 'mail_admins'],
            'level': 'ERROR',
            'propagate': 'True',
        },
        # django.server
        'django.server': {
            'handlers': ['file_errors', 'mail_admins'],
            'level': 'ERROR',
            'propagate': 'True',
        },
        # django.template
        'django.template': {
            'handlers': ['file_errors'],
            'level': 'ERROR',
            'propagate': 'True',
        },
        # django.db_backends
        'django.db_backends': {
            'handlers': ['file_errors'],
            'level': 'ERROR',
            'propagate': 'True',
        },
        # django.security
        'django.security': {
            'handlers': ['file_security'],
            'level': 'INFO',
            'propagate': 'True',
        },
    },
}

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-socola-(d4t_f*r&v@0slmmp3^ho37h&%znr#du3u+6atxc!$c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']

CELERY_IMPORTS = 'news.tasks'
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'fpages',
    'news.apps.NewsConfig',
    'accounts',
    'django_filters',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.google',
]
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'newsproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],

        },
    },
]

WSGI_APPLICATION = 'newsproject.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/news/'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_FORMS = {'signup': 'accounts.models.BasicSignupForm'}
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DEFAULT_FROM_EMAIL = 'caramba.ge@yandex.ru'
EMAIL_HOST = 'smtp.yandex.ru'  # адрес сервера Яндекс-почты для всех один и тот же
EMAIL_PORT = 465  # порт smtp сервера тоже одинаковый
EMAIL_HOST_USER = 'caramba.ge'  # ваше имя пользователя, например, если ваша почта user@yandex.ru, то сюда надо писать user, иными словами, это всё то что идёт до собаки
EMAIL_HOST_PASSWORD = 'fdhocbtlldpnfjkk'  # пароль от почты
EMAIL_USE_SSL = True

STATICFILES_DIRS = [BASE_DIR / "static"]

CACHES = {
    'default': {
        'TIMEOUT': 60,
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),
        # Указываем, куда будем сохранять кэшируемые файлы! Не забываем создать папку cache_files внутри папки с manage.py!
    }
}
