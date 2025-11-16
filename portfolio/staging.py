import os

from .base import *

DEBUG = False

INSTALLED_APPS += ['storages', 's3upload']

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

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "bucket_name": "cw-media-staging-01",
            "custom_domain": "media-staging.carolinewoolard.com",
            "default_acl": "public-read",
            "querystring_auth": False,
        }
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "bucket_name": "cw-static-staging-01",
            "custom_domain": "static-staging.carolinewoolard.com",
            "default_acl": "public-read",
        }
    },
}

SITE_URL = 'https://staging.carolinewoolard.com'

STATIC_URL = 'https://static-staging.carolinewoolard.com/'
MEDIA_URL = 'https://media-staging.carolinewoolard.com/'

STATIC_ROOT = '/tmp/staticfiles'

# AWS S3 Upload Configuration
# Credentials are extracted in base.py from boto3's default credential chain
# In Lambda, this automatically uses the IAM execution role
AWS_STORAGE_BUCKET_NAME = 'cw-media-staging-01'
S3UPLOAD_REGION = 'us-east-1'

S3UPLOAD_DESTINATIONS = {
    'text_pdf': {
        'key': 'texts',
        'allowed_types': ['application/pdf'],
        'allowed_extensions': ['.pdf'],
        'bucket': 'cw-media-staging-01',
    }
}