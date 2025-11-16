from __future__ import unicode_literals

from urllib.parse import urlparse

from django.conf import settings
from django.core.cache import cache
from django.db.models import *
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.html import format_html
from s3upload.fields import S3UploadField
from tinymce.models import HTMLField


class S3UploadFieldWithPath(S3UploadField):
    """
    Custom S3UploadField that returns the path portion instead of the full URL
    for backwards compatibility with FileField behavior.
    """
    def __get__(self, instance, owner=None):
        """Override to return path portion of URL for template compatibility."""
        value = super().__get__(instance, owner)
        if not value or instance is None:
            return value
        # If it's a full URL, extract the path portion
        if isinstance(value, str) and (value.startswith('http://') or value.startswith('https://')):
            parsed = urlparse(value)
            # Return path without leading slash to match FileField behavior
            return parsed.path.lstrip('/')
        # Otherwise it's already a path (legacy data)
        return value



class Base(Model):
    class Meta:
        abstract = True

    name = CharField(max_length=200)
    slug = SlugField(max_length=200)
    created = DateTimeField(auto_now_add=True, editable=False)
    updated = DateTimeField(auto_now=True, editable=False)

    @property
    def url(self):
        return "%s/%s" % (settings.SITE_URL, self.slug)

    def __str__(self):
        return self.name


class BaseWork(Base):
    class Meta:
        abstract = True

    info = CharField(max_length=255, null=True)
    description = HTMLField(blank=True, null=True)
    texts = ManyToManyField('Text', blank=True)
    press = HTMLField(blank=True, null=True)
    is_active = BooleanField(default=True)

class BaseImage(Model):
    class Meta:
        abstract = True

    image = ImageField(upload_to='images', verbose_name='Image')
    order = PositiveSmallIntegerField(default=0)
    is_primary = BooleanField(default=False)
    created = DateTimeField(auto_now_add=True, editable=False)
    updated = DateTimeField(auto_now=True, editable=False)

    @property
    def image_tag(self):
        return format_html('<img src="%s%s" height="100" />' % (settings.MEDIA_URL, self.image))


class ContentBlock(Base):
    class Meta:
        ordering = ['position', 'name']

    content = HTMLField()
    position = PositiveSmallIntegerField(null=True)


class Project(BaseWork):
    class Meta:
        ordering = ['name',]

    system = ForeignKey('System', related_name='project_system', blank=True, null=True, on_delete=CASCADE)
    talks = ManyToManyField('Talk', related_name='project_talks', blank=True)

    @property
    def primary_image(self):
        qs = self.projectimage_set.filter(is_primary=1)
        if len(qs) > 0:
            return qs[0]
        return None


class System(BaseWork):
    class Meta:
        ordering = ['name',]

    project = ForeignKey('Project', related_name='system_project', blank=True, null=True, on_delete=CASCADE)
    talks = ManyToManyField('Talk', related_name='system_talks', blank=True)

    @property
    def primary_image(self):
        qs = self.systemimage_set.filter(is_primary=1)
        if len(qs) > 0:
            return qs[0]
        return None


class Talk(BaseWork):
    class Meta:
        verbose_name = 'Media'
        verbose_name_plural = 'Media'
        ordering = ['name',]

    project = ForeignKey('Project', related_name='talk_project', blank=True, null=True, on_delete=CASCADE)
    system = ForeignKey('System', related_name='talk_system', blank=True, null=True, on_delete=CASCADE)
    talks = ManyToManyField('self', related_name='talk_talks', blank=True)
    link = URLField()

    @property
    def primary_image(self):
        qs = self.talkimage_set.filter(is_primary=1)
        if len(qs) > 0:
            return qs[0]
        return None


class Text(Base):
    class Meta:
        ordering = ['category', 'name']

    TEXT = 'tx'
    TEACHING = 'teaching'

    CATEGORY_CHOICES = (
        (TEXT, 'Text'),
        (TEACHING, 'Teaching')
    )

    description = HTMLField(blank=True, null=True)
    pdf = S3UploadFieldWithPath(dest='text_pdf', blank=True, null=True)
    category = CharField(max_length=20, choices=CATEGORY_CHOICES, default=TEXT)

    @property
    def is_teaching(self):
        return self.category == TEACHING


class Event(Base):
    class Meta:
        ordering = ['date', 'name']

    date = DateTimeField()
    description = HTMLField(null=True, blank=True)
    link = URLField()


class Portfolio(Base):
    class Meta:
        ordering = ['name',]


class ProjectImage(BaseImage):
    project = ForeignKey('Project', on_delete=CASCADE)


class SystemImage(BaseImage):
    system = ForeignKey('System', on_delete=CASCADE)


class TalkImage(BaseImage):
    class Meta:
        verbose_name = 'Media Image'
        verbose_name_plural = 'Media Images'

    talk = ForeignKey('Talk', on_delete=CASCADE)


class PortfolioImage(BaseImage):
    class Meta:
        verbose_name = 'Portfolio Image'
        verbose_name_plural = 'Portfolio Images'
        ordering = ['order',]

    portfolio = ForeignKey('Portfolio', on_delete=CASCADE)
    name = CharField(max_length=200, null=True, blank=True)
    caption = CharField(max_length=200, null=True, blank=True)
    is_active = BooleanField(default=True)
    project = ForeignKey(Project, blank=True, null=True, on_delete=CASCADE)
    system = ForeignKey(System, blank=True, null=True, on_delete=CASCADE)

    @property
    def has_url(self):
        if self.project or self.system:
            return True
        return False

    @property
    def url(self):
        if self.project:
            return reverse('base:project-detail', kwargs={'slug':self.project.slug})

        if self.system:
            return reverse('base:system-detail', kwargs={'slug':self.system.slug})

        return None

@receiver([post_save, post_delete])
def clear_the_cache(**kwargs):
    cache.clear()