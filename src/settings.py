"""
Django settings for src project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("SECRET_KEY")

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ["161.35.14.145", 'localhost', 'pipaytech.com', 'www.pipaytech.com', 'dashboard.nm.161-35-14-145.nip.io']

ROOT_URLCONF = f'{config("PROJECT_NAME")}.urls'

WSGI_APPLICATION = f'{config("PROJECT_NAME")}.wsgi.application'

#ASGI_APPLICATION = f'{config("PROJECT_NAME")}.routing.application'

# Application definition

INSTALLED_APPS = [

    #'cloudinary_storage',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #'cloudinary',
    
    
    
    #installed apps
    
    'user',
    'pipay',
    'scheduler',

    #django alllauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    #django phonenumber
    'phonenumber_field',
    'django_babel',
    
    #django-schedule
    'django_apscheduler',
    
    #django-mptt
    'mptt',
    
    #notifications
    'notifications',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django.contrib.staticfiles.middleware.StaticFilesMiddleware',
]

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

                "pipay.views.currency",
            ],

        },
    },
]


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

AUTH_USER_MODEL = 'user.CustomUser'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# django allauth
SITE_ID = 1

LOGIN_REDIRECT_URL = '/'
ACCOUNT_FORMS = {'signup': 'user.forms.CustomSignupForm'}
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "false"
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/account/login'
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_SESSION_REMEMBER = None

PHONENUMBER_DB_FORMAT = 'NATIONAL'
PHONENUMBER_DEFAULT_REGION = 'NG'

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    STATIC_URL = 'static/'
    #MEDIA_URL = 'media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, "media_cdn")
    STATIC_ROOT = os.path.join(BASE_DIR, "static_cdn")

    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, STATIC_URL),
        #os.path.join(BASE_DIR, MEDIA_URL)
    )
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': config("DB_NAME"),
            'USER': config("DB_USER"),
            'PASSWORD': config("DB_PASSWORD"),
            'HOST': 'localhost',
            'PORT': '',
        }
    }

    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_ENDPOINT_URL = config('AWS_S3_ENDPOINT_URL')
    AWS_QUERYSTRING_AUTH = False
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }
    AWS_LOCATION = "static/"

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
    ]


    AWS_DEFAULT_ACL = 'public-read'

    #STATIC_URL = '{}/{}/'.format(AWS_S3_ENDPOINT_URL, AWS_LOCATION)

    #STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
    STATIC_URL = 'https://%s/%s/' % (AWS_S3_ENDPOINT_URL, AWS_LOCATION)
    TEMP = os.path.join(BASE_DIR, 'temp')
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    """

    CLOUDINARY_STORAGE = {
        'CLOUD_NAME': 'dkbhpgwwo',
        'API_KEY': '238455699553498',
        'API_SECRET': 'pSIi_UQPGzIupwjrRm7e1eGk-08',
        'SECURE': True,
        'MEDIA_TAG': 'media',
        'INVALID_VIDEO_ERROR_MESSAGE': 'Please upload a valid video file.',
        'EXCLUDE_DELETE_ORPHANED_MEDIA_PATHS': (),
        'STATIC_TAG': 'static',
        'STATICFILES_MANIFEST_ROOT': os.path.join(BASE_DIR, 'manifest'),
        'STATIC_IMAGES_EXTENSIONS': ['jpg', 'jpe', 'jpeg', 'jpc', 'jp2', 'j2k', 'wdp', 'jxr',
                                    'hdp', 'png', 'gif', 'webp', 'bmp', 'tif', 'tiff', 'ico'],
        'STATIC_VIDEOS_EXTENSIONS': ['mp4', 'webm', 'flv', 'mov', 'ogv' ,'3gp' ,'3g2' ,'wmv' ,
                                    'mpeg' ,'flv' ,'mkv' ,'avi'],
        'MAGIC_FILE_PATH': 'magic'
    }

    MEDIA_URL = '/media/'  # or any prefix you choose
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

    STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'

    #STATICFILES_DIRS = [
    #    os.path.join(BASE_DIR, 'static')
    #]
    """
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE =True

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = config('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    DEFAULT_FROM_EMAIL = 'Pipaytech Team <noreply@pipaytech.com>'


    BASE_URL = "pipaytech.com"

    # settings.py

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'file': {
                'level': 'ERROR',
                'class': 'logging.FileHandler',
                'filename': '/var/log/django_logs/error.log',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['file'],
                'level': 'ERROR',
                'propagate': True,
            },
        },
    }
