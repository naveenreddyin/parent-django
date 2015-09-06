# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_auto_20150902_1642'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='registration_id',
            new_name='regid',
        ),
    ]
