from django.db import models


# Create your models here.
class DishType(models.Model):
    typeId=models.CharField(max_length=200, null=True)
    name=models.CharField(max_length=20)
    type_image=models.ImageField(upload_to='types')
    # dish=models.ManyToManyField(Dish,related_name='dish_type')
    created_time = models.DateTimeField(auto_now_add=True)
    fix_time = models.DateTimeField(auto_now_add=True)

class Dish(models.Model):
    new_choices=(
        (0,'notNew'),
        (1,'isNew'),
    )
    recommend_choices=(
        (0,'nomarl'),
        (1, 'medium'),
        (2, 'large'),
    )
    spicy_choices=(
        (0,'nomarl'),
        (1, 'medium'),
        (2, 'large'),
    )
    sell_choices=(
        (0,'notSell'),
        (1,'isSell'),
    )
    dishId = models.CharField(max_length=200, null=True)
    name=models.CharField(max_length=20)
    description=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    default_image=models.ImageField(upload_to='dishes')
    is_new=models.SmallIntegerField(default=0,choices=new_choices)
    is_recommend=models.SmallIntegerField(default=0,choices=recommend_choices)
    is_spicy=models.SmallIntegerField(default=0,choices=spicy_choices)
    is_selling=models.SmallIntegerField(default=1,choices=sell_choices)
    created_time = models.DateTimeField(auto_now_add=True)
    fix_time = models.DateTimeField(auto_now_add=True)
    typeid=models.ForeignKey(DishType, on_delete=models.PROTECT,related_name="dish_all_types",default=None)



class DishImage(models.Model):
    dish= models.ForeignKey(Dish, on_delete=models.PROTECT,related_name="dish_all_images")
    image=models.ImageField(upload_to='dishes')
    created_time = models.DateTimeField()
    fix_time = models.DateTimeField()

class DishDisplayInTurn(models.Model):
    dish= models.ForeignKey(Dish, on_delete=models.PROTECT,related_name="dish_display_in_turn")
    image=models.ImageField(upload_to='play')
    index=models.SmallIntegerField(default=0)##the order of play

class DishDisPlay(models.Model):
    dish= models.ForeignKey(Dish, on_delete=models.PROTECT,related_name="dish_display")
    type=models.ForeignKey(DishType,on_delete=models.PROTECT,related_name="type_display")
    image=models.ImageField(upload_to='play')
    index=models.SmallIntegerField(default=0)##the order of play