# Generated by Django 3.1.1 on 2021-09-19 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choices', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
