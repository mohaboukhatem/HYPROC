# Generated by Django 3.1.4 on 2020-12-17 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webSite', '0007_auto_20201217_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='nom',
            field=models.CharField(max_length=50, null='true'),
        ),
    ]