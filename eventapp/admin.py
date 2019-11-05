from django.contrib import admin
from eventapp.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    search_fields = ('title', 'start_time')
    list_display = ('title', 'description', 'start_time', 'end_time')
