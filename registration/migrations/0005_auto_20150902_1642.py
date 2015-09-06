# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_auto_20150902_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.IntegerField()),
                ('registration_id', models.OneToOneField(to='registration.GoogleRegistrationId')),
            ],
        ),
        migrations.RemoveField(
            model_name='typeofuser',
            name='registration_id',
        ),
        migrations.AlterField(
            model_name='connectmodel',
            name='child_device',
            field=models.OneToOneField(related_name='child', to='registration.User'),
        ),
        migrations.AlterField(
            model_name='connectmodel',
            name='parent_device',
            field=models.ForeignKey(related_name='parent', to='registration.User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_profile',
            field=models.OneToOneField(to='registration.UserProfile'),
        ),
        migrations.DeleteModel(
            name='TypeOfUser',
        ),
    ]
