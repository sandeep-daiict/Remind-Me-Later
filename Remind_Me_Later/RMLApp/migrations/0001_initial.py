# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RemindMe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remind_message', models.TextField()),
                ('remind_date', models.DateTimeField(verbose_name='date published')),
                ('remind_email', models.EmailField(max_length=254, blank=True)),
                ('remind_phone', models.CharField(max_length=15, blank=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
            ],
        ),
    ]
