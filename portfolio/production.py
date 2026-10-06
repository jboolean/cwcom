import os

from .base import *

DEBUG = False

INSTALLED_APPS += ['storages', 's3upload']

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

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache',
        'TIMEOUT': None
    },
}

# Also sent as the page's Cache-Control max-age, so this is how stale browsers
# and the CDN can be. The server-side cache is cleared on every save anyway.
CACHE_MIDDLEWARE_SECONDS = 60

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "bucket_name": "cw-media-production",
            "custom_domain": "media.carolinewoolard.com",
            "default_acl": "public-read",
            "querystring_auth": False,
        }
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "bucket_name": "cw-static-production-01",
            "custom_domain": "static.carolinewoolard.com",
            "default_acl": "public-read",
        }
    },
}

SITE_URL = 'https://carolinewoolard.com'

STATIC_URL = 'https://static.carolinewoolard.com/'
MEDIA_URL = 'https://media.carolinewoolard.com/'

STATIC_ROOT = '/tmp/staticfiles'

# AWS S3 Upload Configuration
# Credentials are extracted in base.py from boto3's default credential chain
# In Lambda, this automatically uses the IAM execution role
AWS_STORAGE_BUCKET_NAME = 'cw-media-production'
S3UPLOAD_REGION = 'us-east-1'

S3UPLOAD_DESTINATIONS = {
    'text_pdf': {
        'key': 'texts',
        'allowed_types': ['application/pdf'],
        'allowed_extensions': ['.pdf'],
        'bucket': 'cw-media-production',
        'auth': s3upload_staff_only,
    },
    'images': {
        'key': 'images',
        'allowed_types': ['image/jpeg', 'image/png', 'image/gif', 'image/webp'],
        'allowed_extensions': ['.jpg', '.jpeg', '.png', '.gif', '.webp'],
        'bucket': 'cw-media-production',
        'auth': s3upload_staff_only,
    },
}