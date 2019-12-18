from django.contrib import admin
from songapp.models import Song


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'author')
