from django.contrib import admin
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE
from .models import (
    ContentBlock,
    Portfolio,
    PortfolioImage,
    ProjectImage,
    Project,
    System,
    SystemImage,
    Talk,
    TalkImage,
    Text,
    Event
)


class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage
    verbose_name = 'Portfolio Image'
    verbose_name_plural = 'Portfolio Images'
    fields = ('image', 'image_tag', 'order', 'name', 'caption', 'project', 'system')
    readonly_fields = ('image_tag',)
    extra = 1


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    verbose_name = 'Project Image'
    verbose_name_plural = 'Project Images'
    fields = ('image', 'image_tag', 'order', 'is_primary')
    readonly_fields = ('image_tag',)
    extra = 1


class SystemImageInline(admin.TabularInline):
    model = SystemImage
    verbose_name = 'System Image'
    verbose_name_plural = 'System Images'
    fields = ('image', 'image_tag', 'order', 'is_primary')
    readonly_fields = ('image_tag',)
    extra = 1


class TalkImageInline(admin.TabularInline):
    model = TalkImage
    verbose_name = 'Talk Image'
    verbose_name_plural = 'Talk Images'
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
    inlines = [ SystemImageInline, ]
    exclude = ('images',)


class TalkAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('url',)
    list_display = ('name', 'url')
    inlines = [ TalkImageInline, ]
    exclude = ('images',)


class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('url',)
    list_display = ('name', 'date', 'link', 'url')


class PortfolioAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name',)
    inlines = [ PortfolioImageInline, ]
    exclude = ('images',)


admin.site.register(ContentBlock, ContentBlockAdmin)
admin.site.register(Text, TextAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(PortfolioImage)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)
admin.site.register(System, SystemAdmin)
admin.site.register(SystemImage)
admin.site.register(Talk, TalkAdmin)
admin.site.register(TalkImage)
admin.site.register(Event, EventAdmin)