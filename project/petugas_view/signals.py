import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Log_Aktivitas, Tanggapan
from masyarakat_view.models import Pengaduan

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Tanggapan)
def log_tanggapan(sender, instance, created, **kwargs):
    if created:
        Log_Aktivitas.objects.create(
            petugas=instance.petugas,
            aktifitas=f"Menambahkan tanggapan pada pengaduan ID {instance.pengaduan.id}."
        )

@receiver(post_save, sender=Pengaduan)
def log_pengaduan(sender, instance, **kwargs):
    # Menambahkan log ketika status pengaduan berubah
    Log_Aktivitas.objects.create(
        petugas=instance.petugas,
        aktifitas=f"Status pengaduan ID {instance.id} diubah menjadi {instance.status}."
    )
