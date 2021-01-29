# Generated by Django 3.1.4 on 2020-12-19 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webSite', '0012_auto_20201219_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demandetravailchefsection',
            name='chefsection',
            field=models.ForeignKey(null='true', on_delete=django.db.models.deletion.SET_NULL, to='webSite.chefsection'),
        ),
        migrations.RemoveField(
            model_name='ordretravail',
            name='ouvrier',
        ),
        migrations.AddField(
            model_name='ordretravail',
            name='ouvrier',
            field=models.ManyToManyField(null='true', to='webSite.ouvrier'),
            preserve_default='true',
        ),
    ]
