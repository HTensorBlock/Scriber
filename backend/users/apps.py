from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    label = 'users'
    verbose_name = 'Users App'
    verbose_name_plural = 'Users Apps'
