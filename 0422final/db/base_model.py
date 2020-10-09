from django.db import models

class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='creating time')
    update_time = models.DateTimeField(auto_now=True,verbose_name='updating time')
    is_delete = models.BooleanField(default=False,verbose_name='deleting marks')

    class Meta:
        abstract = True