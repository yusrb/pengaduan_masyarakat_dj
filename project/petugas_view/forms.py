from django import forms
from .models import Tanggapan

class TanggapanForm(forms.ModelForm):
    class Meta:
        model = Tanggapan
        fields = ['tanggapan']
        widgets = {
            'isi_tanggapan': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        }
