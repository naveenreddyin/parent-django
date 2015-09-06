# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerparentapp',
            name='phone_no',
            field=models.CharField(unique=True, max_length=254),
        ),
    ]
