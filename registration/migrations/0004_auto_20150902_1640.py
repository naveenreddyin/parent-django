# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20150902_1639'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RegisterAppPhoneNo',
            new_name='User',
        ),
    ]
