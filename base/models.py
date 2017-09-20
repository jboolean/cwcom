from __future__ import unicode_literals
from django.conf import settings
from django.db.models import *
from django.utils.html import format_html
from tinymce.models import HTMLField


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
        return format_html('<img src="/static/uploads/%s" height="100" />' % self.image)


class ContentBlock(Base):
    class Meta:
        ordering = ['position', 'name']

    content = HTMLField()
    position = PositiveSmallIntegerField(null=True)


class Project(BaseWork):
    class Meta:
        ordering = ['name',]

    system = ForeignKey('System', related_name='project_system', blank=True, null=True)
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

    project = ForeignKey('Project', related_name='system_project', blank=True, null=True)
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

    project = ForeignKey('Project', related_name='talk_project', blank=True, null=True)
    system = ForeignKey('System', related_name='talk_system', blank=True, null=True)
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
    pdf = FileField(upload_to='texts', blank=True, null=True)
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


class ProjectImage(BaseImage):
    project = ForeignKey('Project')


class SystemImage(BaseImage):
    system = ForeignKey('System')


class TalkImage(BaseImage):
    class Meta:
        verbose_name = 'Media Image'
        verbose_name_plural = 'Media Images'

    talk = ForeignKey('Talk')
