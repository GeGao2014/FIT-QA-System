# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-26 13:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AskPete', '0003_auto_20171004_1310'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(max_length=200)),
                ('isAddress', models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='inputtext',
            name='question',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answer_text',
        ),
        migrations.DeleteModel(
            name='InputText',
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AskPete.Question'),
        ),
    ]
