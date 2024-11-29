from django.contrib import admin
from .models import Masyarakat, Jenis_Laporan ,Pengaduan
from petugas_view.models import Petugas
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

@admin.register(Masyarakat)
class MasyarakatAdmin(admin.ModelAdmin):
    exclude = ('is_active', 'is_staff', 'is_superuser')

@admin.register(Jenis_Laporan)
class JenisLaporanAdmin(admin.ModelAdmin):
    pass

@admin.register(Pengaduan)
class PengaduanAdmin(admin.ModelAdmin):
    # list_display = ('nik', 'tgl_pengaduan', 'status', 'dinas')
    exclude = ['status']
    readonly_fields = ['tanggapan']

    def has_add_permission(self, request):
        return request.user.is_staff

    def has_change_permission(self, request, obj=None):
        return request.user.is_staff

    def has_delete_permission(self, request, obj=None):
        return request.user.is_staff

    def has_view_permission(self, request, obj=None):
        return request.user.is_staff