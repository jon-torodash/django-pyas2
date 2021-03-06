# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-01 10:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pyas2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pyas2.Organization'),
        ),
        migrations.AlterField(
            model_name='message',
            name='partner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pyas2.Partner'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='encryption_key',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pyas2.PrivateKey'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='signature_key',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='org_s', to='pyas2.PrivateKey'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='encryption_cert',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pyas2.PublicCertificate'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='signature_cert',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='partner_s', to='pyas2.PublicCertificate'),
        ),
    ]
