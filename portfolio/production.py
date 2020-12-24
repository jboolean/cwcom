from .base import *
import os

DEBUG = False

INSTALLED_APPS += ['storages']

ALLOWED_HOSTS = ['.execute-api.us-east-1.amazonaws.com', '.carolinewoolard.com']

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

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'base.storages.S3StaticStorage'
AWS_STORAGE_BUCKET_NAME = 'cw-media-production'
AWS_STATIC_BUCKET_NAME = 'cw-static-production-01'
AWS_DEFAULT_ACL = 'public-read'
AWS_QUERYSTRING_AUTH = False


SITE_URL = 'https://12scbeayu9.execute-api.us-east-1.amazonaws.com/dev/'

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
MEDIA_URL = 'https://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME