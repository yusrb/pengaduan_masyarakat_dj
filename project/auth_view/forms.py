from django import forms
from masyarakat_view.models import Masyarakat
from petugas_view.models import Petugas
from dinas_view.models import Dinas
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class MasyarakatLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-input rounded-md border-gray-300 w-full py-2 px-4',
            'placeholder': 'Masukkan username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-input rounded-md border-gray-300 w-full py-2 px-4',
            'placeholder': 'Masukkan password'
        })
    )

class MasyarakatCreationForm(UserCreationForm):
    class Meta:
        model = Masyarakat
        fields = ('username', 'password1', 'password2', 'alamat', 'kecamatan', 'telp')
    
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-input rounded-md border-gray-300 w-full mt-1',
            'placeholder': 'Masukkan username'
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-input rounded-md border-gray-300 w-full mt-1',
            'placeholder': 'Masukkan password'
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-input rounded-md border-gray-300 w-full mt-1',
            'placeholder': 'Konfirmasi password'
        })
    )
    alamat = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-input rounded-md border-gray-300 w-full mt-1',
            'placeholder': 'Masukkan alamat'
        })
    )
    kecamatan = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-input rounded-md border-gray-300 w-full mt-1',
            'placeholder': 'Masukkan kecamatan'
        })
    )
    telp = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-input rounded-md border-gray-300 w-full mt-1',
            'placeholder': 'Masukkan nomor telepon'
        })
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if Masyarakat.objects.filter(username=username).exists():
            raise forms.ValidationError("Username sudah digunakan.")
        return username

class PetugasLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username', 
        widget=forms.TextInput(attrs={'class': 'form-input rounded-md border-gray-300', 'placeholder': 'Masukkan username'})
    )
    password = forms.CharField(
        label='Password', 
        widget=forms.PasswordInput(attrs={'class': 'form-input rounded-md border-gray-300', 'placeholder': 'Masukkan password'})
    )

    def confirm_login_allowed(self, user):
        if user.level not in ['admin', 'petugas']:
            raise forms.ValidationError("Hanya admin atau petugas yang dapat login di sini.", code='invalid_login')

class PetugasCreationForm(UserCreationForm):
    class Meta:
        model = Petugas
        fields = ['nama', 'username', 'telp', 'dinas', 'password1', 'password2']

    nama = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-input rounded-md border-gray-300 w-full', 
            'placeholder': 'Masukkan nama'
        })
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-input rounded-md border-gray-300 w-full', 
            'placeholder': 'Masukkan username'
        })
    )
    telp = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-input rounded-md border-gray-300 w-full', 
            'placeholder': 'Masukkan nomor telepon'
        })
    )
    dinas = forms.ModelChoiceField(
        queryset=Dinas.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-input rounded-md border-gray-300 w-full',
        }),
        empty_label="Pilih Instansi"
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-input rounded-md border-gray-300 w-full', 
            'placeholder': 'Masukkan password'
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-input rounded-md border-gray-300 w-full', 
            'placeholder': 'Konfirmasi password'
        })
    )
