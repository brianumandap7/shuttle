# Generated by Django 3.1.1 on 2021-12-10 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0027_hdf_qr_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
