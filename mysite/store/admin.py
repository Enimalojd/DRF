from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Service, UserServiceRelation, Category


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'price', 'available', 'created', 'updated']
    list_display_links = ['id', 'title']
    search_fields = ['id', 'title']
    list_filter = ['available', 'created', 'updated', 'price']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(UserServiceRelation)
class UserServiceRelationAdmin(ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}