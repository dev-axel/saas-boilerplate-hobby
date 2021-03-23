# Generated by Django 3.1.7 on 2021-03-23 07:10

import django.contrib.postgres.fields.citext
from django.contrib.postgres.operations import CITextExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210304_1649'),
    ]

    operations = [
        CITextExtension(),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=django.contrib.postgres.fields.citext.CIEmailField(max_length=255, unique=True, verbose_name='email address'),
        ),
    ]
