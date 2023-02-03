from django.contrib import admin

# Register your models here.
from .models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('id', 'title', 'description')
    list_per_page = 20


admin.site.register(Teacher, TeacherAdmin)
