# Generated by Django 5.0.2 on 2024-02-08 11:03

import status.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0002_rename_user_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=status.models.upload_status_image),
        ),
    ]
