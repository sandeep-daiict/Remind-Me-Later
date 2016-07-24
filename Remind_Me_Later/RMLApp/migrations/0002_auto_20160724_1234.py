# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RMLApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remindme',
            name='remind_date',
            field=models.DateTimeField(verbose_name='date to Remind'),
        ),
    ]
