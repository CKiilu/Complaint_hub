# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-26 14:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicComplaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('First Year', 'First Year'), ('Second Year', 'Second Year'), ('Third Year', 'Third Year'), ('Fourth Year', 'Fourth Year'), ('Fifth Year', 'Fifth Year')], max_length=50)),
                ('semester', models.CharField(choices=[('First Semester', 'First Semester'), ('Second Semester', 'Second Semester')], max_length=50)),
                ('session', models.CharField(max_length=50)),
                ('request_type', models.CharField(choices=[('Makeup', 'Makeup'), ('Portal', 'Portal'), ('Special', 'Special'), ('Result', 'Result')], max_length=50)),
                ('request', models.TextField(max_length=50)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courses', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Exeat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('First Year', 'First Year'), ('Second Year', 'Second Year'), ('Third Year', 'Third Year'), ('Fourth Year', 'Fourth Year'), ('Fifth Year', 'Fifth Year')], max_length=50)),
                ('exeat_type', models.CharField(choices=[('Home', 'Home'), ('Other', 'Other')], max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('application', models.TextField()),
                ('parent_contact', models.CharField(max_length=16)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complaints.Department')),
            ],
        ),
        migrations.CreateModel(
            name='PPD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('First Year', 'First Year'), ('Second Year', 'Second Year'), ('Third Year', 'Third Year'), ('Fourth Year', 'Fourth Year'), ('Fifth Year', 'Fifth Year')], max_length=50)),
                ('hall', models.CharField(max_length=50)),
                ('room', models.CharField(max_length=50)),
                ('site', models.CharField(max_length=50)),
                ('request', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program', models.CharField(max_length=60)),
                ('courses', models.ManyToManyField(to='complaints.Course')),
            ],
        ),
        migrations.CreateModel(
            name='SpecialAdmRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('First Year', 'First Year'), ('Second Year', 'Second Year'), ('Third Year', 'Third Year'), ('Fourth Year', 'Fourth Year'), ('Fifth Year', 'Fifth Year')], max_length=50)),
                ('hall', models.CharField(max_length=50)),
                ('room', models.CharField(max_length=50)),
                ('request', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complaints.Department')),
            ],
        ),
        migrations.CreateModel(
            name='StaffProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matric', models.CharField(max_length=10)),
                ('full_name', models.CharField(max_length=50)),
                ('level', models.CharField(choices=[('First Year', 'First Year'), ('Second Year', 'Second Year'), ('Third Year', 'Third Year'), ('Fourth Year', 'Fourth Year'), ('Fifth Year', 'Fifth Year')], max_length=50)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complaints.Program')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WorkStudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('First Year', 'First Year'), ('Second Year', 'Second Year'), ('Third Year', 'Third Year'), ('Fourth Year', 'Fourth Year'), ('Fifth Year', 'Fifth Year')], max_length=50)),
                ('semester', models.CharField(choices=[('First Semester', 'First Semester'), ('Second Semester', 'Second Semester')], max_length=50)),
                ('session', models.CharField(max_length=50)),
                ('application', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complaints.Department')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complaints.StudentProfile')),
            ],
        ),
        migrations.AddField(
            model_name='specialadmrequest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complaints.StudentProfile'),
        ),
        migrations.AddField(
            model_name='ppd',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complaints.StudentProfile'),
        ),
        migrations.AddField(
            model_name='exeat',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complaints.StudentProfile'),
        ),
        migrations.AddField(
            model_name='department',
            name='programs',
            field=models.ManyToManyField(to='complaints.Program'),
        ),
        migrations.AddField(
            model_name='academiccomplaint',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='complaints.Course'),
        ),
        migrations.AddField(
            model_name='academiccomplaint',
            name='course_lecturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complaints.StaffProfile', to_field='full_name'),
        ),
        migrations.AddField(
            model_name='academiccomplaint',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complaints.Department'),
        ),
        migrations.AddField(
            model_name='academiccomplaint',
            name='program',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='complaints.Program'),
        ),
        migrations.AddField(
            model_name='academiccomplaint',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complaints.StudentProfile'),
        ),
    ]
