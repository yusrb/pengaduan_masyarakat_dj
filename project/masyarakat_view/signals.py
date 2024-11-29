from django.db.models.signals import post_save
from django.dispatch import receiver
from petugas_view.models import Tanggapan

@receiver(post_save, sender=Tanggapan)
def update_pengaduan_status(sender, instance, **kwargs):
    instance.pengaduan.status = instance.status
    instance.pengaduan.save()
