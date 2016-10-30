from django.contrib import admin
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE
from .models import (
    ContentBlock,
    ProjectImage,
    Project,
    System,
    Talk,
    Text,
    Event
)


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    verbose_name = 'Project Image'
    verbose_name_plural = 'Project Images'
    fields = ('image', 'image_tag', 'order', 'is_primary')
    readonly_fields = ('image_tag',)
    extra = 1


class ContentBlockAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('url',)
    list_display = ('name', 'position', 'url')
    list_editable = ('position',)


class TextAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('url',)
    list_display = ('name', 'url')


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('url',)
    list_display = ('name', 'url')
    inlines = [ ProjectImageInline, ]
    exclude = ('images',)


class SystemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('url',)
    list_display = ('name', 'url')


class TalkAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('url',)
    list_display = ('name', 'url')


class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('url',)
    list_display = ('name', 'date', 'link', 'url')


admin.site.register(ContentBlock, ContentBlockAdmin)
admin.site.register(Text, TextAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)
admin.site.register(System, SystemAdmin)
admin.site.register(Talk, TalkAdmin)
admin.site.register(Event, EventAdmin)