# Generated by Django 3.1.5 on 2021-01-22 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20210122_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='hashed_id',
            field=models.CharField(blank=True, max_length=16, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='hashed_id',
            field=models.CharField(blank=True, max_length=16, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='hashed_id',
            field=models.CharField(blank=True, max_length=16, null=True, unique=True),
        ),
    ]
