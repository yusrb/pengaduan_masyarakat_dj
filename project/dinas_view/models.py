from django.db import models

class Dinas(models.Model):
  nama = models.CharField(max_length=35)
  telp = models.CharField(max_length=13)

  class Meta:
    verbose_name = "Dinas"
    verbose_name_plural = "Dinas"

  def __str__(self):
    return self.nama