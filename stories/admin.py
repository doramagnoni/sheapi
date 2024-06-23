from django.contrib import admin
from .models import Story

class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'updated_at')

admin.site.register(Story, StoryAdmin)


# Register your models here.
