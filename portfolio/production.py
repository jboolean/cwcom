from .base import *

DEBUG = False

INSTALLED_APPS += ['storages']

ALLOWED_HOSTS = ['.execute-api.us-east-1.amazonaws.com', '.carolinewoolard.com']

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
AWS_STORAGE_BUCKET_NAME = 'cw-media-production'
AWS_STATIC_BUCKET_NAME = 'cw-static-production-01'
AWS_DEFAULT_ACL = 'public-read'
AWS_QUERYSTRING_AUTH = False


SITE_URL = 'https://12scbeayu9.execute-api.us-east-1.amazonaws.com/dev/'

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
MEDIA_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME