# Generated by Django 5.1.2 on 2024-10-25 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AddField(
            model_name='user',
            name='my_id',
            field=models.BigAutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
