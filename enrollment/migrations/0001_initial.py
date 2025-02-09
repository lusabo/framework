# Generated by Django 5.1.4 on 2025-01-23 17:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DietaryHabits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SleepDuration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_birth', models.DateField()),
                ('gender', models.CharField(max_length=50)),
                ('academic_pressure', models.IntegerField()),
                ('work_pressure', models.IntegerField()),
                ('cgpa', models.FloatField()),
                ('study_satisfaction', models.IntegerField()),
                ('job_satisfaction', models.IntegerField()),
                ('suicidal_thoughts', models.BooleanField()),
                ('work_study_hour', models.IntegerField()),
                ('financial_strees', models.IntegerField()),
                ('family_history_mental_illness', models.BooleanField()),
                ('risk_of_drepession', models.FloatField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='enrollment.city')),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='enrollment.degree')),
                ('dietary_habits', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='enrollment.dietaryhabits')),
                ('profession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='enrollment.profession')),
                ('sleep_duration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='enrollment.sleepduration')),
            ],
        ),
    ]
