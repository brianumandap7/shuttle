# Generated by Django 3.1.1 on 2021-12-09 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0026_auto_20211209_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='hdf',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
