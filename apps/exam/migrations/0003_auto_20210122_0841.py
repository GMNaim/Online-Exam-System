# Generated by Django 3.1.5 on 2021-01-22 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_auto_20210122_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='hashed_id',
            field=models.CharField(blank=True, default='7830917f6d924d2d', max_length=16, null=True, unique=True),
        ),
    ]
