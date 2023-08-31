from django.contrib import admin
from .models import Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    list_filter = ('price',)


admin.site.register(Service, ServiceAdmin)
