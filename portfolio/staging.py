from .base import *
import os

DEBUG = False

INSTALLED_APPS += ['storages']

ALLOWED_HOSTS = ['.execute-api.us-east-1.amazonaws.com', '.staging.carolinewoolard.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_DATABASE'),
        'USER': os.environ.get('DB_USERNAME'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache',
        'TIMEOUT': None
    },
}

CACHE_MIDDLEWARE_SECONDS = 7 * 24 * 60 * 60

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'base.storages.S3StaticStorage'
AWS_STORAGE_BUCKET_NAME = 'cw-media-staging-01'
AWS_STATIC_BUCKET_NAME = 'cw-static-staging-01'
AWS_DEFAULT_ACL = 'public-read'
AWS_QUERYSTRING_AUTH = False


SITE_URL = 'https://staging.carolinewoolard.com'

AWS_S3_CUSTOM_DOMAIN = 'media.staging.carolinewoolard.com'
AWS_STATIC_CUSTOM_DOMAIN = 'static.staging.carolinewoolard.com'
STATIC_URL = 'https://static.staging.carolinewoolard.com/'
MEDIA_URL = 'https://media.staging.carolinewoolard.com/'