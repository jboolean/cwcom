from __future__ import unicode_literals

from django.apps import AppConfig


class BaseConfig(AppConfig):
    name = 'base'
    
    def ready(self):
        """Monkey patch django-s3-upload to support AWS session tokens."""
        try:
            from django.conf import settings
            from s3upload import utils

            # Store original function
            original_create_upload_data = utils.create_upload_data
            
            def patched_create_upload_data(*args, **kwargs):
                """Add session token if available in settings."""
                if 'token' not in kwargs and hasattr(settings, 'AWS_SESSION_TOKEN') and settings.AWS_SESSION_TOKEN:
                    kwargs['token'] = settings.AWS_SESSION_TOKEN
                return original_create_upload_data(*args, **kwargs)
            
            # Replace the function
            utils.create_upload_data = patched_create_upload_data
        except ImportError:
            # s3upload not installed, skip patching
            pass