from django.contrib import admin
from .models import Dinas

@admin.register(Dinas)
class DinasAdmin(admin.ModelAdmin):

    def get_model_perms(self, request):
        perms = super().get_model_perms(request)
        if request.user.__class__.__name__ == 'Masyarakat':
            return {}
        return perms
