# Generated by Django 4.1.7 on 2023-12-04 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0002_perevalareas_perevalimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='SprActivitiesTypes',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
            ],
            options={
                'db_table': 'spr_activities_types',
            },
        ),
    ]
