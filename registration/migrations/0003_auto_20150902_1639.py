# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20150826_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConnectModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='GoogleRegistrationId',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('registration_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RegisterAppPhoneNo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_no', models.CharField(unique=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.IntegerField()),
                ('registration_id', models.OneToOneField(to='registration.GoogleRegistrationId')),
            ],
        ),
        migrations.DeleteModel(
            name='RegisterParentApp',
        ),
        migrations.AddField(
            model_name='registerappphoneno',
            name='user_profile',
            field=models.OneToOneField(to='registration.TypeOfUser'),
        ),
        migrations.AddField(
            model_name='connectmodel',
            name='child_device',
            field=models.OneToOneField(related_name='child', to='registration.TypeOfUser'),
        ),
        migrations.AddField(
            model_name='connectmodel',
            name='parent_device',
            field=models.ForeignKey(related_name='parent', to='registration.TypeOfUser'),
        ),
    ]
