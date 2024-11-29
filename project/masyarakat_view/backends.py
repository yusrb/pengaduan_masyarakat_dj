from django.contrib.auth.backends import BaseBackend
from masyarakat_view.models import Masyarakat

class MasyarakatBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Masyarakat.objects.get(username=username)
            if user.check_password(password):
                return user
        except Masyarakat.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Masyarakat.objects.get(pk=user_id)
        except Masyarakat.DoesNotExist:
            return None
