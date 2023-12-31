# Generated by Django 4.0.2 on 2023-09-01 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('creator', models.EmailField(max_length=254)),
                ('players', models.JSONField()),
                ('config', models.JSONField()),
                ('waiting', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
