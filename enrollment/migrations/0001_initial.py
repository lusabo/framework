# Generated by Django 5.1.4 on 2025-01-18 14:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_birth', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], max_length=10)),
                ('enrollment_number', models.CharField(max_length=10)),
                ('marital_status', models.CharField(choices=[('Solteiro', 'Solteiro'), ('Casado', 'Casado'), ('Divorciado', 'Divorciado'), ('Viúvo', 'Viúvo')], max_length=15)),
                ('children', models.BooleanField(default=False)),
                ('disabled', models.BooleanField(default=False)),
                ('mode_transportation', models.CharField(choices=[('Carro', 'Carro'), ('Transporte público', 'Transporte público'), ('A pé', 'A pé'), ('Bicicleta', 'Bicicleta'), ('Outros', 'Outros')], max_length=30)),
                ('household_size', models.PositiveIntegerField()),
                ('annual_household_income', models.FloatField()),
                ('defaulter', models.BooleanField(default=False)),
                ('default_risk', models.CharField(choices=[('Baixo', 'Baixo'), ('Médio', 'Médio'), ('Alto', 'Alto')], default='Baixo', max_length=5)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enrollment.course')),
            ],
        ),
    ]
