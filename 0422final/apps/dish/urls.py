
from django.contrib import admin
from django.urls import path, include
from dish import views

app_name = 'dish'
urlpatterns = [
    path('',views.show_homepage,name='home'),
    path('get_dish',views.show_dishes,name='get_dish'),
    path('get_photo/<int:id>', views.get_photo, name='get_photo'),
]
