# from django.contrib import admin
# from django.urls import path, include
# from user import views
#
# app_name = 'user'
# urlpatterns = [
#     path('register', views.register_action, name='register'),
#     path('login', views.login_action, name='login'),
#     path('logout', views.logout_action, name='logout'),
#     path('active/<token>', views.active_action, name='active'),
#     path('centre_information', views.centre_information, name='centre_information'),
#     path('centre_order/(?P<page>\d+)', views.centre_order, name='centre_order'),
#     path('centre_address', views.centre_address, name='centre_address'),
#     path('other_address/<int:id>', views.other_address, name='other_address'),
#
# ]

from django.contrib import admin
from django.urls import path, include
from user import views

app_name = 'user'
urlpatterns = [
    path('register', views.register_action, name='register'),
    path('login', views.login_action, name='login'),
    path('logout', views.logout_action, name='logout'),
    # path('active/<token>', views.active_action, name='active'),
    path('centre_information', views.centre_information, name='centre_information'),
    path('centre_order_detail/<int:id>', views.centre_order_detail, name='centre_order_detail'),
    path('centre_order_list', views.centre_order_list, name='centre_order_list'),
    path('centre_address', views.centre_address, name='centre_address'),
    path('other_address/<int:id>', views.other_address, name='other_address'),
    path('active/<slug:username>/<slug:token>',
         views.active_action, name='active'),
]