from django.contrib import admin

# Register your models here.
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    list_filter = ('title',)
    search_fields = ('id','title')
    list_per_page = 20

admin.site.register(Service, ServiceAdmin)