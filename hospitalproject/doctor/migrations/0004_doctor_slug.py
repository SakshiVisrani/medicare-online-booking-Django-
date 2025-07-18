# Generated by Django 5.2.1 on 2025-07-13 09:44

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_doctor_next_available_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, default='', editable=False, populate_from='name', unique=True),
        ),
    ]
