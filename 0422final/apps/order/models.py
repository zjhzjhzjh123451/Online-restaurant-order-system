from django.db import models


# Create your models here.

class Order(models.Model):
    status_choices = (
            (0, 'not pay'),
            (1, 'has paid'),
        )
    orderId=models.CharField(max_length=200, null=True)
    user = models.ForeignKey('user.User', default=None, on_delete=models.PROTECT)
    address = models.ForeignKey('user.Address', default=None, on_delete=models.PROTECT, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    status = models.SmallIntegerField(default=0, choices=status_choices)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=None, null=True)


class OrderDishes(models.Model):
    order = models.ForeignKey(Order, default=None, on_delete=models.PROTECT)
    dish = models.ForeignKey('dish.Dish', default=None, on_delete=models.PROTECT)
    count = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=None, null=True)
    comment = models.CharField(max_length=300,null=True)
