from django.contrib import admin
from .models import DateLink

@admin.register(DateLink)
class DateLinkAdmin(admin.ModelAdmin):
    list_display = ('date', 'url')
    ordering = ('date',)
