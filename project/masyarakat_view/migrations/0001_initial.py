# Generated by Django 5.1.3 on 2024-11-29 10:43

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dinas_view', '0001_initial'),
        ('petugas_view', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jenis_Laporan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Masyarakat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('alamat', models.TextField()),
                ('kecamatan', models.CharField(max_length=35)),
                ('telp', models.CharField(max_length=13)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Masyarakat',
                'verbose_name_plural': 'Masyarakat',
            },
        ),
        migrations.CreateModel(
            name='Pengaduan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tgl_pengaduan', models.DateTimeField(auto_now_add=True)),
                ('isi_aduan', ckeditor.fields.RichTextField()),
                ('foto', models.ImageField(upload_to='gambar_pengaduan/')),
                ('status', models.CharField(blank=True, choices=[('0', 'Belum Terjawab'), ('desposisi', 'Desposisi'), ('proses', 'Proses'), ('selesai', 'Selesai'), ('tolak', 'Tolak')], default='0', max_length=10, null=True)),
                ('dinas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dinas_view.dinas')),
                ('jenis_laporan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='masyarakat_view.jenis_laporan')),
                ('tanggapan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petugas_view.tanggapan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masyarakat_view.masyarakat')),
            ],
            options={
                'verbose_name': 'Pengaduan',
                'verbose_name_plural': 'Pengaduan',
            },
        ),
    ]
