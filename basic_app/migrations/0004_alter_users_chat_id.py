# Generated by Django 4.2.11 on 2024-05-05 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='chat_id',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]