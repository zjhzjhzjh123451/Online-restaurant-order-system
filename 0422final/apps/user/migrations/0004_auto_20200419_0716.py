# Generated by Django 3.0.2 on 2020-04-19 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200419_0647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='addr',
            field=models.CharField(default='5030 Centre Avenue', max_length=260),
        ),
        migrations.AlterField(
            model_name='address',
            name='phone',
            field=models.CharField(default='1234567890', max_length=12),
        ),
        migrations.AlterField(
            model_name='address',
            name='receiver',
            field=models.CharField(default='yy', max_length=20),
        ),
    ]
