# Generated by Django 3.1.1 on 2021-10-21 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
