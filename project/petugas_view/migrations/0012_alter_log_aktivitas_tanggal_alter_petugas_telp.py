# Generated by Django 5.1.3 on 2024-11-30 09:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petugas_view', '0011_alter_log_aktivitas_tanggal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log_aktivitas',
            name='tanggal',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 30, 9, 43, 19, 626695, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='petugas',
            name='telp',
            field=models.CharField(max_length=13),
        ),
    ]
