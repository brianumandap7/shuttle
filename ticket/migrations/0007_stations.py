# Generated by Django 3.1.1 on 2021-11-29 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0006_easy_maps'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stations',
            fields=[
                ('station_id', models.AutoField(primary_key=True, serialize=False)),
                ('longlat', models.CharField(blank=True, max_length=255, null=True)),
                ('current_loc', models.CharField(blank=True, max_length=255, null=True)),
                ('driver', models.CharField(blank=True, max_length=255, null=True)),
                ('shuttle', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]