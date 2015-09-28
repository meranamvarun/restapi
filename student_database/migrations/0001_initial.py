# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='marks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('registration_no', models.IntegerField(verbose_name='Registration No')),
                ('marks_in_x', models.IntegerField(verbose_name='Marks_In_X')),
                ('marks_in_xii', models.IntegerField(verbose_name='Marks_In_XII')),
                ('cgpi', models.IntegerField(verbose_name='CGPI')),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10, verbose_name='Student Name')),
                ('roll_no', models.IntegerField(verbose_name='Roll No')),
                ('branch', models.CharField(max_length=5, verbose_name='Branch of Student')),
                ('mobile_no', models.IntegerField(verbose_name='Mobile No')),
                ('registration_no', models.ForeignKey(related_name='registartion_num_student', verbose_name='Registration No', to='student_database.marks')),
            ],
        ),
        migrations.CreateModel(
            name='StudentContactDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email_id', models.CharField(max_length=256, verbose_name='Email Id')),
                ('address', models.CharField(max_length=200, verbose_name='Student Address')),
                ('mobile_no', models.ForeignKey(related_name='mobile_number', verbose_name='Mobile No', to='student_database.student')),
            ],
        ),
    ]
