from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'type_meet', 'time', 'place', 'created_at']
    list_display_links = ['author', 'type_meet', 'time', 'place', 'created_at']

    