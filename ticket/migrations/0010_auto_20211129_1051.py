# Generated by Django 3.1.1 on 2021-11-29 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0009_shuttle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stations',
            name='shuttle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ticket.shuttle'),
        ),
    ]
