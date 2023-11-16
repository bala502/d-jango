# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-11-06 08:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=35)),
                ('district', models.CharField(db_column='District', max_length=20)),
                ('population', models.IntegerField(db_column='Population')),
            ],
            options={
                'db_table': 'city',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('code', models.CharField(db_column='Code', max_length=3, primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=52)),
                ('continent', models.CharField(db_column='Continent', max_length=13)),
                ('region', models.CharField(db_column='Region', max_length=26)),
                ('surfacearea', models.FloatField(db_column='SurfaceArea')),
                ('indepyear', models.SmallIntegerField(blank=True, db_column='IndepYear', null=True)),
                ('population', models.IntegerField(db_column='Population')),
                ('lifeexpectancy', models.FloatField(blank=True, db_column='LifeExpectancy', null=True)),
                ('gnp', models.FloatField(blank=True, db_column='GNP', null=True)),
                ('gnpold', models.FloatField(blank=True, db_column='GNPOld', null=True)),
                ('localname', models.CharField(db_column='LocalName', max_length=45)),
                ('governmentform', models.CharField(db_column='GovernmentForm', max_length=45)),
                ('headofstate', models.CharField(blank=True, db_column='HeadOfState', max_length=60, null=True)),
                ('capital', models.IntegerField(blank=True, db_column='Capital', null=True)),
                ('code2', models.CharField(db_column='Code2', max_length=2)),
            ],
            options={
                'db_table': 'country',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(default='female', max_length=100)),
                ('email', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Countrylanguage',
            fields=[
                ('countrycode', models.ForeignKey(db_column='CountryCode', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='world.Country')),
                ('language', models.CharField(db_column='Language', max_length=30)),
                ('isofficial', models.CharField(db_column='IsOfficial', max_length=1)),
                ('percentage', models.FloatField(db_column='Percentage')),
            ],
            options={
                'db_table': 'countrylanguage',
                'managed': False,
            },
        ),
    ]
