from django.contrib import admin

from .models import *


class WomanAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('id', 'name')
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Woman, WomanAdmin)
admin.site.register(Category, CategoryAdmin)
