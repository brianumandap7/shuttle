# Generated by Django 3.1.1 on 2021-12-09 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0019_tracing'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracing',
            name='hdf_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]