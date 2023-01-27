from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class WomanAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'title', 'time_create', 'get_html_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}
    fields = ('title', 'slug', 'category', 'content', 'photo', 'get_html_photo', 'is_published', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = 'Photo'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('id', 'name')
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Woman, WomanAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Website about Famous Women'
admin.site.site_header = 'Website about Famous Women'
