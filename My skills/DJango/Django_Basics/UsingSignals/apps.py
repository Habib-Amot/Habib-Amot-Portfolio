from django.apps import AppConfig

class UsingsignalsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'UsingSignals'

    def ready(self):
        from UsingSignals import signals
        return super().ready()
