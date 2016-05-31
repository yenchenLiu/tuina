"""
Django settings for MemberSystem project.

Generated by 'django-admin startproject' using Django 1.9.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
from MemberSystem import env
from django.utils.translation import ugettext_lazy as _

LANGUAGES = [
    ('zh-hant', _('Traditional Chinese')),
    ('en-us', 'English'),
]

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOCALE_PATHS = [os.path.join(BASE_DIR, "locale")]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.DEBUG

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user',
    'consumer',
    'medical_record',
    'reservation.apps.ReservationConfig'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MemberSystem.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'MemberSystem.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = env.DATABASES

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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

SUIT_CONFIG = {
    # header
    'ADMIN_NAME': '昊德深層經絡按摩會員系統',
    'HEADER_DATE_FORMAT': 'Y-m-d (l)',
    'HEADER_TIME_FORMAT': 'H:i',

    # forms
    'SHOW_REQUIRED_ASTERISK': True,
    'CONFIRM_UNSAVED_CHANGES': True,

    # menu
    'SEARCH_URL': '/admin/user/customer/',
    # 'MENU_ICONS': {
    #     'sites': 'icon-leaf',
    #     'auth': 'icon-lock',
    #     'user': 'icon-user',
    # },
    'MENU_OPEN_FIRST_CHILD': True,  # Default True
    'MENU_EXCLUDE': ('auth.group',),
    'MENU': (
        'sites',
        {'app': 'auth', 'label': "帳戶", 'icon': 'icon-lock', 'models': ('user',)},
        {'app': 'user', 'label': _('profile'), 'icon': 'icon-user', 'models': ('Customer', 'CustomerPhone', 'Master')},
        {'app': 'medical_record', 'label': "病歷紀錄", 'icon': 'icon-user',
         'models': ('Complaint', 'Massage')},
        {'app': 'consumer', 'label': "消費記錄", 'icon': 'icon-user', 'models': ('MembershipCard', 'ExpensesRecord')},
        {'app': 'reservation', 'label': "預約記錄", 'icon': 'icon-user',
         'models': ('Reservation', {'label': '時間軸', 'url': '/admin/reservation_timeline/'},)},
        {'app': 'reservation', 'label': "電話記錄", 'icon': 'icon-user',
         'models': ({'label': "電話紀錄", 'url': '/phone/'},)},
    ),

    # misc
    'LIST_PER_PAGE': 20
}

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'zh-Hant'

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
