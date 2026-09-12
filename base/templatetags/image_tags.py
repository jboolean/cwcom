from django.conf import settings
from django import template
register = template.Library()


# Roughly based on https://medium.com/hceverything/applying-srcset-choosing-the-right-sizes-for-responsive-images-at-different-breakpoints-a0433450a4a3
# And the widths of the thumbnail images
WIDTHS = [350, 700, 1366, 1600, 1920]

@register.filter
def srcset(file_or_url):
    if isinstance(file_or_url, str):
        # S3UploadField values are bare paths (e.g. "images/foo.jpg"),
        # not absolute URLs, so they need MEDIA_URL prefixed.
        url = file_or_url if file_or_url.startswith(('http://', 'https://')) else settings.MEDIA_URL + file_or_url
    else:
        url = file_or_url.url
    return ', '.join(list(map(lambda w: '%s?width=%d %dw' % (url, w, w), WIDTHS)) + [url+'?width=full'])
