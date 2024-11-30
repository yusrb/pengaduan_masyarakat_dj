from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from django.contrib.auth.hashers import check_password, make_password

class PetugasManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("The Username field must be set")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)

class Petugas(AbstractBaseUser):
    nama = models.CharField(max_length=35)
    username = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=128)
    level = models.CharField(max_length=10, choices=[('admin', 'Admin'), ('petugas', 'Petugas')], default='petugas', null=True, blank=True)
    telp = models.CharField(max_length=13)
    dinas = models.ForeignKey('dinas_view.Dinas', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)

    objects = PetugasManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['level']

    class Meta:
        verbose_name = "Petugas"
        verbose_name_plural = "Petugas"

    def __str__(self):
        return self.username

    def set_password(self, raw_password):
        super().set_password(raw_password)

    def check_password(self, raw_password):
        return super().check_password(raw_password)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.last_login = timezone.now()
        super().save(*args, **kwargs)

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff

class Log_Aktivitas(models.Model):
  petugas = models.ForeignKey(Petugas, on_delete=models.CASCADE)
  aktifitas = models.CharField(max_length=255)
  tanggal = models.DateTimeField(default=timezone.now())

  class Meta:
    verbose_name = "Log Aktifitas"
    verbose_name_plural = "Log Aktifitas"
    ordering = ['-tanggal']

  def __str__(self):
    return f"Petugas: {self.petugas}, Aktivitas: {self.aktifitas}, Tanggal: {self.tanggal.strftime('%Y-%m-%d %H:%M:%S')}"

class Tanggapan(models.Model):
  pengaduan = models.ForeignKey('masyarakat_view.Pengaduan', on_delete=models.CASCADE)
  tgl_tanggapan = models.DateTimeField(auto_now_add=True)
  tanggapan = RichTextField()

  petugas = models.ForeignKey(Petugas, on_delete=models.CASCADE)

  class Status(models.TextChoices):
    BELUM_TERJAWAB = '0', 'Belum Terjawab'
    DESPOSISI = 'desposisi', 'Desposisi'
    PROSES = 'proses', 'Proses'
    SELESAI = 'selesai', 'Selesai'
    TOLAK = 'tolak', 'Tolaks'

  status = models.CharField(max_length=9, choices=Status.choices, default=Status.BELUM_TERJAWAB)

  class Meta:
    verbose_name = 'Tanggapan'
    verbose_name_plural = 'Tanggapan'

  def __str__(self):
    return f'Tanggapan Pengaduan pada {self.pengaduan.isi_aduan[:50]}'