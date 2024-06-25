from django.contrib import admin
from .models import Story

class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'content', 'author__username')
    list_filter = ('created_at', 'updated_at')

admin.site.register(Story, StoryAdmin)


# Register your models here.
