import hashlib
from functools import lru_cache

from django import template
from django.contrib.staticfiles import finders
from django.templatetags.static import static

register = template.Library()


@lru_cache(maxsize=None)
def _content_hash(path):
    absolute_path = finders.find(path)
    if not absolute_path:
        return None
    with open(absolute_path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()[:10]


@register.simple_tag
def static_versioned(path):
    """
    Like {% static %}, but appends a hash of the file's contents so browsers
    and CDNs fetch the new file whenever it changes, rather than serving a
    stale cached copy of an unversioned URL.
    """
    url = static(path)
    version = _content_hash(path)
    return '%s?v=%s' % (url, version) if version else url
