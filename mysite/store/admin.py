from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Service, UserServiceRelation


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    list_filter = ('price',)


admin.site.register(Service, ServiceAdmin)


@admin.register(UserServiceRelation)
class UserServiceRelationAdmin(ModelAdmin):
    pass
