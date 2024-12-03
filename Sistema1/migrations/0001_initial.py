# Generated by Django 5.1.1 on 2024-11-02 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='Municipio')),
                ('rut', models.CharField(max_length=20, verbose_name='Rut')),
                ('cuenta', models.CharField(max_length=50, verbose_name='Cuenta')),
            ],
            options={
                'db_table': 'Municipios',
            },
        ),
    ]