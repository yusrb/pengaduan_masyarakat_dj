from django import forms
from .models import Tanggapan

class TanggapanForm(forms.ModelForm):
    class Meta:
        model = Tanggapan
        fields = ['tanggapan',]

    tanggapan = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm hover:ring-lime-200  focus:outline-none focus:ring-lime-200 focus:border-lime-200',
        'rows': 5,
        'placeholder': 'Tulis tanggapan di sini...'
    }), required=True)