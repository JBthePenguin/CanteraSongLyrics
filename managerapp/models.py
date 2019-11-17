from django.contrib.auth.models import User, Permission


class Member(User):
    """ association member """
    pass

    def save(self, *args, **kwargs):
        # auth to connect to admin site and save
        self.is_staff = True
        super(Member, self).save(*args, **kwargs)
        # add permissions for song and event
        auth_apps = ['songapp', 'eventapp']
        for auth_app in auth_apps:
            permissions = Permission.objects.filter(
                content_type__app_label=auth_app)
            for permission in permissions:
                self.user_permissions.add(permission)

    class Meta:
        ordering = ['username']
        verbose_name = "Membre"
        verbose_name_plural = "Membres"


class Manager(User):
    """ association admin """
    pass

    def save(self, *args, **kwargs):
        # auth to connect to admin site and save
        self.is_staff = True
        super(Manager, self).save(*args, **kwargs)
        # add permissions for song and event
        auth_apps = ['songapp', 'eventapp']
        for auth_app in auth_apps:
            permissions = Permission.objects.filter(
                content_type__app_label=auth_app)
            for permission in permissions:
                self.user_permissions.add(permission)
        # add permission for managerapp member model
        permissions = Permission.objects.filter(
            content_type__model='member')
        for permission in permissions:
            self.user_permissions.add(permission)

    class Meta:
        ordering = ['username']
        verbose_name = "Administrateur"
        verbose_name_plural = "Administrateurs"
