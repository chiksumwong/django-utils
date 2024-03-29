"""
Django settings for server project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!f!irhb8f@szpxt7+&kaiokz__&rg6udxwe^aktoqxk=tb8l#$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third Party Apps
    'rest_framework',
    'corsheaders',
    'django_apscheduler',
    # APP
    'scheduler_email'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
        'DIRS': [os.path.join(BASE_DIR, 'scheduler_email', 'templates')],
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

WSGI_APPLICATION = 'server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django-lab',
        'USER': 'root',
        'PASSWORD': 'Asd^14556123',
        'HOST': '192.168.0.197',
        'PORT': '3307',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Hong_Kong'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ==================================================
# REST_FRAMEWORK
# ==================================================
REST_FRAMEWORK = {
    # Default Permission
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],

    # API Version Control
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    'ALLOWED_VERSIONS': ['a_email_v1'],
}


# ==================================================
# CORS
# ==================================================
CORS_ALLOWED_ORIGINS = []


# ==================================================
# Logging
# ==================================================
# FILE_LOGGING = env.bool('FILE_LOGGING', True)
# SYSTEM_DEBUG = env.bool('SYSTEM_DEBUG', True)
FILE_LOGGING = True
SYSTEM_DEBUG = True


def check_file_logging_filter(record):
    return FILE_LOGGING


def check_system_debug_filter(record):
    return SYSTEM_DEBUG


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{asctime}  [{levelname}]  {pathname}  <{funcName}>  {message}',
            'style': '{',
        },
        'simple': {
            'format': '{asctime}  [{levelname}]  {message}',
            'style': '{',
        }
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_file_logging_true': {
            '()': 'django.utils.log.CallbackFilter',
            'callback': check_file_logging_filter,
        },
        'require_system_debug_true': {
            '()': 'django.utils.log.CallbackFilter',
            'callback': check_system_debug_filter,
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
            'filters': ['require_debug_true']
        }
    },
    'loggers': {
        'system': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}


if FILE_LOGGING:
    LOG_ROOT = os.path.join(BASE_DIR, 'logs')
    Path(LOG_ROOT).mkdir(parents=True, exist_ok=True)
    LOGGING['handlers']['file.error'] = {
        'class': 'logging.FileHandler',
        'level': 'ERROR',
        'formatter': 'verbose',
        'filename': os.path.join(LOG_ROOT, 'error.log'),
        'filters': ['require_file_logging_true']
    }
    LOGGING['handlers']['file.debug'] = {
        'class': 'logging.FileHandler',
        'level': 'DEBUG',
        'formatter': 'verbose',
        'filename': os.path.join(LOG_ROOT, 'debug.log'),
        'filters': ['require_file_logging_true', 'require_system_debug_true']
    }
    LOGGING['handlers']['file_email'] = {
        'class': 'logging.FileHandler',
        'level': 'DEBUG',
        'formatter': 'verbose',
        'filename': os.path.join(LOG_ROOT, 'email.log'),
        'filters': ['require_file_logging_true', 'require_system_debug_true']
    }
    LOGGING['loggers'] = {
        'system': {
            'handlers': ['console', 'file.error', 'file.debug'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'system.email': {
            'handlers': ['console', 'file_email'],
            'level': 'DEBUG',
            'propagate': False,
        }
    }


# ==================================================
# SMTP Configuration
# ==================================================


# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'dnd.samwong@gmail.com'
# EMAIL_HOST_PASSWORD = ''

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = 'email_send.log'
EMAIL_HOST_USER = 'cswong@example.com.hk'
