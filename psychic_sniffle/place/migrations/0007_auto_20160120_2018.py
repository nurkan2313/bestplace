# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0006_placepicture'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='placepicture',
            options={'verbose_name': '\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435', 'verbose_name_plural': '\u0413\u0430\u043b\u0435\u0440\u0435\u044f'},
        ),
        migrations.AlterField(
            model_name='placepicture',
            name='picture',
            field=models.ImageField(upload_to='uploads/places/', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435'),
        ),
    ]