from django.contrib import admin
from .models import Petugas, Log_Aktivitas, Tanggapan

@admin.register(Petugas)
class PetugasAdmin(admin.ModelAdmin):
  def get_model_perms(self, request):
    perms = super().get_model_perms(request)

    if request.user.level == 'petugas':
      return {}

    if request.user.__class__.__name__=='Masyarakat':
      return {}
    return perms

@admin.register(Log_Aktivitas)
class Log_Aktifitas_Admin(admin.ModelAdmin):
  def get_model_perms(self, request):
    perms = super().get_model_perms(request)

    if request.user.__class__.__name__=='Masyarakat':
      return {}

    if request.user.level == 'petugas':
      return {}
    return perms

@admin.register(Tanggapan)
class TanggapanAdmin(admin.ModelAdmin):
  def get_model_perms(self, request):
    perms = super().get_model_perms(request)

    if request.user.__class__.__name__=='Masyarakat':
      return {}
    return perms