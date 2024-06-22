from django.contrib import admin
from .models import Story

class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at', 'category')
    search_fields = ('title', 'author__username', 'category')
    list_filter = ('created_at', 'updated_at', 'category')

admin.site.register(Story, StoryAdmin)


# Register your models here.
