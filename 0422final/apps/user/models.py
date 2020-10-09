from django.db import models
from django.contrib.auth.models import AbstractUser
from db.base_model import BaseModel

# Create your models here.
class User(AbstractUser):
    point=models.IntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    fix_time = models.DateTimeField(auto_now_add=True)

# class Address(models.Model):
#     created_by=models.ForeignKey(User,default=None,on_delete=models.PROTECT)
#     is_default=models.BooleanField(default=False)
#     content=models.CharField(max_length=200)
#     phone_number=models.CharField(max_length=20)
#     receiver=models.CharField(max_length=20)
#     created_time = models.DateTimeField()
#     fix_time=models.DateTimeField()
class Address(BaseModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT,default="")
    receiver = models.CharField(max_length=20,default="yy")
    addr = models.CharField(max_length=260,default="5030 Centre Avenue")
    zip_code = models.CharField(max_length=6,null=True)
    phone = models.CharField(max_length=12,default="1234567890")
    is_default = models.BooleanField(default=False)
    # def get_default_address(user):
    #     a = Address.objects.get(user=user)
    #     return a.addr

    class Meta:
        db_table = 'df_address'
        verbose_name = 'address_n'
        verbose_name_plural = verbose_name

