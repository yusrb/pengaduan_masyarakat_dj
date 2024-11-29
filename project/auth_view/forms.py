from django import forms
from masyarakat_view.models import Masyarakat
from petugas_view.models import Petugas
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class MasyarakatCreationForm(UserCreationForm):
    class Meta:
        model = Masyarakat
        fields = ('username', 'password1', 'password2', 'alamat', 'kecamatan', 'telp')

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if Masyarakat.objects.filter(username=username).exists():
            raise forms.ValidationError("Username sudah digunakan.")
        return username

class PetugasLoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if user.level not in ['admin', 'petugas']:
            raise forms.ValidationError("Hanya admin atau petugas yang dapat login di sini.", code='invalid_login')

class PetugasCreationForm(UserCreationForm):
    class Meta:
        model = Petugas
        fields = ['nama', 'username', 'telp', 'level', 'dinas']