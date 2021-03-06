# Generated by Django 3.0.2 on 2020-04-19 21:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200325_0047'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0002_auto_20200324_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdishes',
            name='comment',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderId', models.CharField(max_length=200, null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.SmallIntegerField(choices=[(0, 'not pay'), (1, 'has paid')], default=0)),
                ('total', models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True)),
                ('address', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='user.Address')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='orderdishes',
            name='order',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='order.Order'),
        ),
        migrations.DeleteModel(
            name='OrderInformation',
        ),
    ]
