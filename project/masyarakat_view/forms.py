from django import forms
from .models import Pengaduan
from dinas_view.models import Dinas
from django.forms import ModelForm

class PengaduanForm(ModelForm):
    class Meta:
        model = Pengaduan
        fields = ['isi_aduan', 'foto', 'dinas']

    isi_aduan = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-input px-4 py-2 border w-full border w-full-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-lime-500',
        'rows': 4,
        'placeholder': 'Tulis aduan Anda di sini'
    }))
    foto = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={
        'class': 'form-input py-2 px-4 border w-full border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-lime-500'
    }))
    dinas = forms.ModelChoiceField(queryset=Dinas.objects.all(), widget=forms.Select(attrs={
        'class': 'form-input py-2 px-4 border w-full border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-lime-500'
    }))
