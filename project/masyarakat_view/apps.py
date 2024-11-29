from django.apps import AppConfig


class MasyarakatViewConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'masyarakat_view'

    def ready(self):
        import masyarakat_view.signals

