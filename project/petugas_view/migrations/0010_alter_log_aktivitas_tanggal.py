# Generated by Django 5.1.3 on 2024-11-30 09:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petugas_view', '0009_alter_log_aktivitas_tanggal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log_aktivitas',
            name='tanggal',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 30, 9, 41, 8, 919217, tzinfo=datetime.timezone.utc)),
        ),
    ]
