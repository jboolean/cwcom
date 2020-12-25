from django.conf import settings

from storages.backends.s3boto3 import S3ManifestStaticStorage

# Allows a separate bucket for static files from media files
# By default they are in the same bucket which seems scary
class S3StaticStorage(S3ManifestStaticStorage):
    bucket_name = settings.AWS_STATIC_BUCKET_NAME
    custom_domain = settings.AWS_STATIC_CUSTOM_DOMAIN

