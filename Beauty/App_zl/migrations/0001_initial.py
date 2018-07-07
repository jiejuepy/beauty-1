# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-04 01:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_tel', models.CharField(max_length=11)),
                ('u_provinces', models.CharField(max_length=1024)),
                ('u_city', models.CharField(max_length=1024)),
                ('u_county', models.CharField(max_length=1024)),
                ('u_street', models.CharField(max_length=1024)),
                ('u_email', models.CharField(max_length=1024)),
                ('u_detailaddr', models.CharField(max_length=4096)),
                ('u_addrstatus', models.IntegerField()),
            ],
            options={
                'db_table': 'address',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_account', models.CharField(max_length=50)),
                ('a_pwd', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'admin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_num', models.IntegerField()),
                ('is_select', models.IntegerField()),
            ],
            options={
                'db_table': 'cart',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(blank=True, max_length=50, null=True)),
                ('c_code', models.IntegerField(blank=True, null=True)),
                ('c_desc', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'g_category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GCategory2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c2_name', models.CharField(blank=True, max_length=50, null=True)),
                ('c2_desc', models.CharField(blank=True, max_length=255, null=True)),
                ('c2_code', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'g_category2',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_code', models.IntegerField()),
                ('c2_code', models.IntegerField()),
                ('g_name', models.CharField(max_length=50)),
                ('g_desc', models.CharField(blank=True, max_length=255, null=True)),
                ('g_info', models.CharField(blank=True, max_length=255, null=True)),
                ('g_mktprice', models.CharField(max_length=20)),
                ('g_price', models.CharField(max_length=20)),
                ('g_goodsprops', models.CharField(blank=True, max_length=255, null=True)),
                ('g_pics', models.CharField(blank=True, max_length=255, null=True)),
                ('g_inventory', models.IntegerField()),
                ('g_sale', models.IntegerField()),
                ('g_status', models.IntegerField()),
                ('g_createtime', models.DateTimeField(blank=True, null=True)),
                ('g_changetime', models.DateTimeField(blank=True, null=True)),
                ('g_class', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'goods',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Goodsorder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'goodsorder',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_price', models.FloatField()),
                ('o_status', models.IntegerField()),
                ('o_creattime', models.DateTimeField()),
                ('o_changetime', models.DateTimeField()),
                ('o_num', models.IntegerField()),
            ],
            options={
                'db_table': 'orders',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=1024)),
                ('u_pwd', models.CharField(max_length=1024)),
                ('u_tel', models.IntegerField(blank=True, null=True)),
                ('u_ticket', models.TextField()),
                ('u_outtime', models.DateTimeField()),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]