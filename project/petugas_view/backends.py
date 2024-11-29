from django.contrib.auth.backends import BaseBackend
from petugas_view.models import Petugas

class PetugasBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Petugas.objects.get(username=username)
            if user.check_password(password):
                return user
        except Petugas.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Petugas.objects.get(pk=user_id)
        except Petugas.DoesNotExist:
            return None
