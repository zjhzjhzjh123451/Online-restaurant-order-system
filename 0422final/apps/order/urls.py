
from django.contrib import admin
from django.urls import path, include
from order import views

app_name = 'order'
urlpatterns = [
    path('order', views.order, name='order'),
    path('ordertest', views.ordertest, name='ordertest'),
    path('checkout', views.checkout, name='checkout'),
    path('order_page/<int:id>', views.order_page, name='order_page'),
    path('success_page/<int:id>', views.success_page, name='success_page'),

]
