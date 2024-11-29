from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from ckeditor.fields import RichTextField

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

class MasyarakatManager(BaseUserManager):
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

class Masyarakat(AbstractBaseUser):
    username = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=128)
    alamat = models.TextField()
    kecamatan = models.CharField(max_length=35)
    telp = models.CharField(max_length=13)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)

    objects = MasyarakatManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['alamat', 'kecamatan', 'telp']

    class Meta:
        verbose_name = "Masyarakat"
        verbose_name_plural = "Masyarakat"

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

class Jenis_Laporan(models.Model):
    jenis = models.CharField(max_length=32)

    def __str__(self):
        return self.jenis

class Pengaduan(models.Model):
    tgl_pengaduan = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Masyarakat, on_delete=models.CASCADE)
    isi_aduan = RichTextField()
    foto = models.ImageField(upload_to="gambar_pengaduan/")
    dinas = models.ForeignKey('dinas_view.Dinas', on_delete=models.CASCADE)

    jenis_laporan = models.ForeignKey(Jenis_Laporan, on_delete=models.SET_NULL, null=True, blank=True)

    class Status(models.TextChoices):
        BELUM_TERJAWAB = '0', 'Belum Terjawab'
        DESPOSISI = 'desposisi', 'Desposisi'
        PROSES = 'proses', 'Proses'
        SELESAI = 'selesai', 'Selesai'
        TOLAK = 'tolak', 'Tolak'

    status = models.CharField(max_length=10, choices=Status.choices, default=Status.BELUM_TERJAWAB, blank=True, null=True)

    class Meta:
        verbose_name = "Pengaduan"
        verbose_name_plural = "Pengaduan"

    def __str__(self):
        return f"Pengaduan oleh {self.user.username} - Status: {self.get_status_display()}"

    @property
    def tanggapan(self):
        return self.tanggapan_set.first()
