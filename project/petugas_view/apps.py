from django.apps import AppConfig


class PetugasViewConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'petugas_view'

    def ready(self):
        import petugas_view.signals