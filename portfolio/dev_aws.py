import os

from .base import *

DEBUG = True

# AWS S3 Configuration
# Credentials are extracted in base.py from boto3's default credential chain
# For local dev, this uses AWS CLI credentials
AWS_STORAGE_BUCKET_NAME = 'cw-media-production'
S3UPLOAD_REGION = 'us-east-1'

INSTALLED_APPS += ['storages', 's3upload']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cw',
        'USER': 'cw',
        'PASSWORD': 'B-c!Mc-q*Xry8mWDQyXCUNABXxdxgX',
        'HOST': 'shared-projects.cioc65o5flzv.us-east-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'base.storages.S3StaticStorage'
AWS_STATIC_BUCKET_NAME = 'cw-static-production-01'
AWS_DEFAULT_ACL = 'public-read'
AWS_QUERYSTRING_AUTH = False


SITE_URL = 'http://127.0.0.1:8000/'

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
MEDIA_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME

# AWS S3 Upload Configuration
S3UPLOAD_DESTINATIONS = {
    'text_pdf': {
        'key': 'texts',
        'allowed_types': ['application/pdf'],
        'allowed_extensions': ['.pdf'],
        'bucket': 'cw-media-production',
    }
}