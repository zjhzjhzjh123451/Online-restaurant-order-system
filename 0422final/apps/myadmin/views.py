from django.http import HttpResponse
from django.urls import reverse
from django.utils import timezone

from django.shortcuts import render, redirect
from user.models import User
from dish.models import Dish, DishType
from order.models import Order, OrderDishes
# Create your views here.
from django.core.paginator import Paginator


def index(request):
    context = {}
    return render(request, 'index.html', context)


##未写分页
def user_list(request):
    # data0 = User.objects.filter(is_active=0)
    # data1 = User.objects.filter(is_active=1)

    # p0 = Paginator(data0, 2)
    # p1 = Paginator(data1, 2)
    #

    # list0 = p0.page(1)
    # list1 = p1.page(1)
    data = User.objects.all()
    # context = {'list0': data0, 'list1': data1}
    context = {'data': data}
    return render(request, 'user_list.html', context)

def user_delete(request, id):
    the_user = User.objects.get(id=id)
    the_user.delete()

    data = User.objects.all()
    context = {'data': data}
    return render(request, 'user_list.html', context)


def user_active(request, id):
    the_user = User.objects.get(id=id)
    the_user.is_active = 1
    the_user.fix_time = timezone.now()
    the_user.save()
    data = User.objects.all()
    context = {'data': data}
    return render(request, 'user_list.html', context)


def user_cancel(request, id):
    the_user = User.objects.get(id=id)
    the_user.is_active = 0
    the_user.fix_time = timezone.now()
    the_user.save()
    data = User.objects.all()
    context = {'data': data}
    return render(request, 'user_list.html', context)


def dish_type_add(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'dish_type_add.html', context)
    if request.method == 'POST':
        data = request.POST.dict()

        if data['name'] == "":
            return HttpResponse('<script>alert("You don\'t write a dish type name.");history.back(-1);</script>')
        the_type_image = request.FILES.get('type_image', None)

        if DishType.objects.filter(name__exact=data['name']):
            return HttpResponse('<script>alert("You should write a different dish type.");history.back(-1);</script>')

        if not the_type_image:
            return HttpResponse('<script>alert("You don\'t upload a type image.");history.back(-1);</script>')


        new_type = DishType(name=data['name'],
                            )
        new_type.type_image = the_type_image
        new_type.save()
        new_type.typeId=new_type.id
        new_type.save()
        return redirect(reverse('myadmin:dish_type_list'))

def dish_add(request):
    types = DishType.objects.all()
    context = {'types':types}
    if request.method == 'GET':


        return render(request, 'dish_add.html', context)
    if request.method == 'POST':
        data = request.POST.dict()
        print(data)
        if data['name'] == "":
            return HttpResponse('<script>alert("You don\'t write a dish name.");history.back(-1);</script>')

        if Dish.objects.filter(name__exact=data['name']):
            return HttpResponse('<script>alert("You should write a different dish.");history.back(-1);</script>')

        if data['price'] == "" :
            return HttpResponse('<script>alert("You don\'t write a dish price.");history.back(-1);</script>')
        try:
            float(data['price'])
        except:
            return HttpResponse('<script>alert("You don\'t write a dish price and it should be a number.");history.back(-1);</script>')
        ##需验证price是否是数字
        the_default_picture = request.FILES.get('default_image', None)
        if not the_default_picture:
            return HttpResponse('<script>alert("You don\'t upload a default image.");history.back(-1);</script>')


        new_dish = Dish(name=data['name'],
                        description=data['description'],
                        price=data['price'],
                        is_new=data['is_new'],
                        is_recommend=data['is_recommend'],
                        is_spicy=data['is_spicy'],
                        is_selling=data['is_selling'],
                        typeid=DishType.objects.get(id=data['typeid']))

        new_dish.default_image = the_default_picture
        new_dish.save()
        new_dish.dishId=new_dish.id
        # print(new_dish.dishId)
        new_dish.save()

        return redirect(reverse('myadmin:dish_list'))


def dish_type_list(request):

    list=DishType.objects.all()
    context={'list':list}
    return render(request, 'dish_type_list.html', context)

def dish_list(request):

    list=Dish.objects.all()
    context={'list':list}
    return render(request, 'dish_list.html', context)


def dish_type_delete(request,id):
    the_dish_type = DishType.objects.get(id=id)
    the_dishes=Dish.objects.filter(typeid=the_dish_type)
    the_dishes.delete()
    the_dish_type.delete()

    list = DishType.objects.all()
    context = {'list': list}
    return render(request, 'dish_type_list.html', context)

def dish_delete(request,id):
    the_dish=Dish.objects.get(id=id)
    the_dish.delete()
    list = Dish.objects.all()
    context = {'list': list}
    return render(request, 'dish_list.html', context)


def dish_type_edit(request,id):

    if request.method == 'GET':
        the_type=DishType.objects.get(id=id)
        context = {'the_type':the_type}
        return render(request, 'dish_type_edit.html', context)
    if request.method == 'POST':
        the_type = DishType.objects.get(id=id)
        data = request.POST.dict()

        if data['name'] == "":
            return HttpResponse('<script>alert("You don\'t write a dish type name.");history.back(-1);</script>')


        if DishType.objects.filter(name__exact=data['name']) and data['name']!=the_type.name:
            return HttpResponse('<script>alert("The name has been used.");history.back(-1);</script>')

        the_type.name=data['name']
        the_type_image = request.FILES.get('type_image', None)
        if  the_type_image:
            the_type.type_image=the_type_image

        the_type.save()

        return redirect(reverse('myadmin:dish_type_list'))



def dish_edit(request,id):

    if request.method == 'GET':
        the_dish = Dish.objects.get(id=id)
        types = DishType.objects.all()
        context = {'types': types, 'the_dish': the_dish}

        return render(request, 'dish_edit.html', context)

    if request.method == 'POST':
        data = request.POST.dict()
        if data['name'] == "":
            return HttpResponse('<script>alert("You don\'t write a dish name.");history.back(-1);</script>')

        if data['price'] == "":
            return HttpResponse('<script>alert("You don\'t write a dish price.");history.back(-1);</script>')
        try:
            float(data['price'])
        except:
            return HttpResponse('<script>alert("You don\'t write a dish price and it should be a number.");history.back(-1);</script>')
        ##需验证price是否是数字

        the_dish = Dish.objects.get(id=id)
        the_dish.name = data['name']
        the_dish.description = data['description']
        the_dish.price = data['price']
        the_dish.is_new = data['is_new']
        the_dish.is_recommend = data['is_recommend']
        the_dish.is_spicy = data['is_spicy']
        the_dish.is_selling = data['is_selling']
        the_dish.typeid = DishType.objects.get(id=data['typeid'])

        the_default_picture = request.FILES.get('default_image', None)
        if  the_default_picture:
            the_dish.default_image = the_default_picture

        the_dish.save()

        return redirect(reverse('myadmin:dish_list'))



def order_list(request):
    list=Order.objects.all()
    context={'list':list}
    return render(request, 'order_list.html', context)


def order_delete(request,id):
    the_order = Order.objects.get(id=id)
    the_order_dishes=OrderDishes.objects.filter(order=the_order)
    the_order_dishes.delete()
    the_order.delete()

    list = Order.objects.all()
    context = {'list': list}
    return render(request, 'order_list.html', context)


def order_details(request,id):
    the_order = Order.objects.get(id=id)
    the_order_dishes=OrderDishes.objects.filter(order=the_order)

    list = the_order_dishes
    context = {'list': list,'the_order':the_order}
    return render(request, 'order_details.html', context)


def myadmin_login(request):
    if request.method=='GET':
        context={}
        return render(request,'myadmin_login.html',context)
    if request.method=='POST':
        if request.POST.get('username')=='42myadmin' and request.POST.get('password')=='42myadmin':
            request.session['AdminUser']={'username':'42myadmin'}
            return redirect(reverse('myadmin:index'))
        else:
            return HttpResponse('<script>alert("accout or password is wrong");location.href="/myadmin/myadmin_login"</script>')

def myadmin_logout(request):
    del request.session['AdminUser']
    return redirect(reverse('myadmin:myadmin_login'))