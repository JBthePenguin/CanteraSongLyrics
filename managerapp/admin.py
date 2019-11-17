from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from managerapp.models import Manager, Member


class ManagerAdminCreationForm(UserCreationForm):
    pass

    class Meta:
        model = Manager
        fields = UserCreationForm.Meta.fields + (
            'first_name', 'last_name', 'email',)


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    form = ManagerAdminCreationForm
    search_fields = ('username',)
    list_display = ('username', 'first_name', 'last_name', 'email')

    def get_app_list(self, request):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """
        app_dict = self._build_app_dict(request)
        # Sort the apps alphabetically.
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())
        # Sort the models alphabetically within each app.
        for app in app_list:
            app['models'].sort(key=lambda x: x['name'])
        return app_list


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    form = ManagerAdminCreationForm
    search_fields = ('username',)
    list_display = ('username', 'first_name', 'last_name', 'email')
