from django.apps import AppConfig


class AuthAppConfig(AppConfig):
    name = 'Auth_App'

from django.apps import AppConfig
from django.db.models.signals import post_migrate

# Ek khali function banayein jo kuch nahi karega
def skip_create_permissions(sender, **kwargs):
    return

class AuthAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Auth_App'

    def ready(self):
        # Permissions create karne wale signal ko disconnect kar dein
        from django.contrib.auth.management import create_permissions
        post_migrate.disconnect(create_permissions, dispatch_uid="django.contrib.auth.management.create_permissions")