# Generated by Django 3.0.2 on 2020-03-25 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='fix_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
