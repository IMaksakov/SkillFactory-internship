# Generated by Django 4.1.7 on 2023-04-18 21:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0002_rename_pereval_perevaladded'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('fam', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('otc', models.CharField(max_length=150)),
                ('phone', models.CharField(blank=True, max_length=14, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed.", regex='^\\+?1?\\d{9,12}$')])),
            ],
        ),
    ]
