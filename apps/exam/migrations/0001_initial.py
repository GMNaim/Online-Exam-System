# Generated by Django 3.1.5 on 2021-01-18 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashed_id', models.CharField(blank=True, max_length=16, null=True, unique=True)),
                ('created_by', models.CharField(blank=True, max_length=500, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('question_text', models.TextField()),
                ('option_1', models.CharField(blank=True, max_length=255, null=True)),
                ('option_2', models.CharField(blank=True, max_length=255, null=True)),
                ('option_3', models.CharField(blank=True, max_length=255, null=True)),
                ('option_4', models.CharField(blank=True, max_length=255, null=True)),
                ('correct_answer', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
