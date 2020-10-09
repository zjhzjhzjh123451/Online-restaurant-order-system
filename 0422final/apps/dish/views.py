from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.core import serializers
from dish.models import Dish, DishType
from django.http import HttpResponse
import json

def show_homepage(request):
    context = {}
    return render(request, 'home.html', context)


def show_dishes(request):

    dishes = serializers.serialize('json', Dish.objects.all())
    dish_types = serializers.serialize('json', DishType.objects.all())
    # print(dish_types.length)
    data = {
        'dishes' : dishes,
        'dish_type' : dish_types,
    }
    return HttpResponse(json.dumps(data),content_type='application/json')

def get_photo(request, id):
    dish = Dish.objects.get(dishId=id)
    return HttpResponse(dish.default_image)