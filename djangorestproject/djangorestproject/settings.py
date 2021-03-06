"""
Django settings for djangorestproject project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from datetime import timedelta
from pathlib import Path
from .utils.ubuntu import getlocaliplist

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p_^(njg+bt+ztk@st6a7gm!@yv3cmpgu8h64!szym_hcd^!h%('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = list(getlocaliplist())

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "rest_framework",
    "restapi",
    "languages",
    "guestbook",
    "urlsexamples",
    "weather",
    "django.contrib.humanize",
    "gameplay",
    "django_extensions",
    "crispy_forms"]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))

ROOT_URLCONF = 'djangorestproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates"), ],
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

WSGI_APPLICATION = 'djangorestproject.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }

    # Use \conninfo to get the details for the database
    # viz.You are connected to database "djangorestproject" as user "postgres"
    # via socket in "/var/run/postgresql" at port "5432".

    "default":
        {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": "djangorestproject",
            "USER": "doogle",
            "PASSWORD": "password",
            "HOST": "localhost",
            "PORT": "5432",
        }
    # {
    #     "ENGINE": "django.db.backends.postgresql_psycopg2",
    #     "NAME": "jinlorzq",
    #     "USER": "jinlorzq",
    #     "PASSWORD": "3E27HuKcAWJblr5i9EGxr6g1xmbHkR47",
    #     "HOST": "tantor.db.elephantsql.com",
    #     "PORT": "5432",
    # }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-IN'

TIME_ZONE = 'Asia/Singapore'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

PROJECT_ROOT = Path(__file__).parents[1]

STATICFILES_DIRS = [os.path.join(PROJECT_ROOT, 'guestbook/static/'), os.path.join(PROJECT_ROOT, 'gameplay/static/')]

LOGIN_REDIRECT_URL = "todoindex"
LOGOUT_REDIRECT_URL = "welcome1"

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_AUTHENTICATION_CLASSES": ("rest_framework_simplejwt.authentication.JWTAuthentication",
                                       'rest_framework.authentication.BasicAuthentication',
                                       'rest_framework.authentication.SessionAuthentication',)
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(seconds=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1)
}

EMAIL_HOST = 'imap.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'debu999@gmail.com'
EMAIL_HOST_PASSWORD = os.environ.get("GMAIL_PWD")
EMAIL_USE_SSL = False
EMAIL_USE_TLS = True
CRISPY_TEMPLATE_PACK = "bootstrap4"
