# Generated by Django 3.0.2 on 2020-04-19 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20200419_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdishes',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True),
        ),
    ]
