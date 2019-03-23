from django.contrib import admin
from main.models import Content

class ContentAdmin(admin.ModelAdmin):
    list_display = ('word', 'number', )

# Register your models here.
admin.site.register(Content, ContentAdmin)