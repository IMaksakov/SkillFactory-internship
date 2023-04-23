# Generated by Django 4.1.7 on 2023-21-03 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerevalAreas',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('id_parent', models.BigIntegerField()),
                ('title', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pereval_areas',
            },
        ),
        migrations.CreateModel(
            name='PerevalImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('img', models.BinaryField()),
            ],
            options={
                'db_table': 'pereval_images',
            },
        ),
    ]
