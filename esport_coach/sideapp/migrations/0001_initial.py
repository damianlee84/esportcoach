# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-27 22:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blacklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('reason', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Champions',
            fields=[
                ('champion', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server', models.CharField(max_length=50)),
                ('champion', models.CharField(max_length=500)),
                ('role', models.CharField(max_length=500)),
                ('pricerate', models.FloatField(default=0.0)),
                ('avatar', models.URLField()),
                ('rating', models.IntegerField(default=0)),
                ('overview', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Coaching',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('pricerate', models.FloatField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('request', models.TextField(blank=True)),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sideapp.Coach')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('date', models.DateTimeField()),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sideapp.Coach')),
            ],
        ),
        migrations.CreateModel(
            name='Reviewing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_stars', models.PositiveIntegerField(null=True)),
                ('communication_stars', models.PositiveIntegerField(null=True)),
                ('helpfulness_stars', models.PositiveIntegerField(null=True)),
                ('comment', models.TextField()),
                ('date', models.DateTimeField()),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sideapp.Coach')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer', models.CharField(max_length=100, null=True)),
                ('skill_stars', models.PositiveIntegerField(null=True)),
                ('communication_stars', models.PositiveIntegerField(null=True)),
                ('helpfulness_stars', models.PositiveIntegerField(null=True)),
                ('comment', models.CharField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('skype', models.CharField(max_length=50)),
                ('mmr', models.PositiveIntegerField(default=0)),
                ('server', models.CharField(max_length=50)),
                ('hero', models.CharField(max_length=50)),
                ('rating', models.PositiveIntegerField(default=0)),
                ('reputation', models.PositiveIntegerField(default=0)),
                ('students', models.PositiveIntegerField(default=0)),
                ('pricerate', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=32)),
                ('transaction_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=18)),
                ('email', models.EmailField(max_length=254)),
                ('pname', models.CharField(max_length=100)),
                ('rank', models.CharField(max_length=100)),
                ('skypeid', models.CharField(max_length=100)),
                ('twitchid', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='reviews',
            name='coach',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sideapp.Signup'),
        ),
        migrations.AddField(
            model_name='reviewing',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sideapp.User'),
        ),
        migrations.AddField(
            model_name='report',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sideapp.User'),
        ),
        migrations.AddField(
            model_name='coaching',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sideapp.User'),
        ),
        migrations.AddField(
            model_name='coach',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sideapp.User'),
        ),
        migrations.AddField(
            model_name='blacklist',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sideapp.User'),
        ),
    ]
