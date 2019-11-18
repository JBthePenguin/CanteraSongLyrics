from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from managerapp.models import Manager, Member


@admin.register(Manager)
class ManagerAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': (
            'username', 'password',
            'first_name', 'last_name', 'email',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')}
         ),
    )
    search_fields = ('username',)
    list_display = ('username', 'first_name', 'last_name', 'email')


# MEMBER
@admin.register(Member)
class MemberAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': (
            'username', 'password',
            'first_name', 'last_name', 'email',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')}
         ),
    )
    search_fields = ('username',)
    list_display = ('username', 'first_name', 'last_name', 'email')
