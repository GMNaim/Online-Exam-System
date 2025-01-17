# Generated by Django 3.1.5 on 2021-01-22 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210122_0841'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashed_id', models.CharField(blank=True, default='bb6a00d0ba6c4f9a', max_length=16, null=True, unique=True)),
                ('created_by', models.CharField(blank=True, max_length=500, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('code', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='hashed_id',
            field=models.CharField(blank=True, default='ae8150fa7fb349da', max_length=16, null=True, unique=True),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashed_id', models.CharField(blank=True, default='bb6a00d0ba6c4f9a', max_length=16, null=True, unique=True)),
                ('created_by', models.CharField(blank=True, max_length=500, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('code', models.CharField(max_length=50, unique=True)),
                ('permission', models.ManyToManyField(related_name='role_permission', to='account.Permission')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
