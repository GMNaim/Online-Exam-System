# Generated by Django 3.1.5 on 2021-01-22 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0007_auto_20210122_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='hashed_id',
            field=models.CharField(blank=True, default='bb6a00d0ba6c4f9a', max_length=16, null=True, unique=True),
        ),
    ]
