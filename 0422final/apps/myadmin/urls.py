from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from myadmin import views

app_name = 'myadmin'
urlpatterns = [
    path('', views.index, name='index'),
    path('user_list', views.user_list, name='user_list'),
    path('user_delete/<int:id>', views.user_delete, name='user_delete'),
    path('user_cancel/<int:id>', views.user_cancel, name='user_cancel'),
    path('user_active/<int:id>', views.user_active, name='user_active'),
    path('dish_type_add', views.dish_type_add, name='dish_type_add'),
    path('dish_add', views.dish_add, name='dish_add'),
    path('dish_type_list', views.dish_type_list, name='dish_type_list'),
    path('dish_list', views.dish_list, name='dish_list'),
    path('dish_delete/<int:id>', views.dish_delete, name='dish_delete'),
    path('dish_type_delete/<int:id>', views.dish_type_delete, name='dish_type_delete'),
    path('dish_edit/<int:id>', views.dish_edit, name='dish_edit'),
    path('dish_type_edit/<int:id>', views.dish_type_edit, name='dish_type_edit'),
    path('order_list', views.order_list, name='order_list'),
    path('order_delete/<int:id>', views.order_delete, name='order_delete'),
    path('order_details/<int:id>', views.order_details, name='order_details'),
    path('myadmin_login',views.myadmin_login,name='myadmin_login'),
    path('myadmin_logout', views.myadmin_logout, name='myadmin_logout'),

]
