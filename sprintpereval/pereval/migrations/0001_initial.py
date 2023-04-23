# Generated by Django 4.1.7 on 2023-21-03 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PerevalAdded',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('raw_data', models.JSONField()),
                ('images', models.JSONField()),
                ('status', models.CharField(choices=[('new', 'New'), ('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='new', max_length=10)),
            ],
            options={
                'db_table': 'pereval_added',
            },
        ),
    ]