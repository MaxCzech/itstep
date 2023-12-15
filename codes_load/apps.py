from django.apps import AppConfig


class CodesLoadConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'codes_load'

    def ready(self):
        import codes_load.signals
