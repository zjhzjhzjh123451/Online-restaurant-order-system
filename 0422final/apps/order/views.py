from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from user import forms
from user.models import User
#from itsdangerous import TimedJSONWebSignatureSerializer, SignatureExpired
from django.conf import settings
from django.core.mail import send_mail
from order.models import Order, OrderDishes
from dish.models import Dish
from user.models import User, Address


def ordertest(request):
    return render(request, 'order.html')


def order(request):
    return render(request, 'order_old.html')


def checkout(request):
    if request.method == 'GET':
        # 可配置下404的页面
        raise Http404("Order does not exist")
    if request.method == 'POST':
        dishes = request.POST.getlist('dish[]')
        numbers = request.POST.getlist('num[]')
        print(request.user.username)
        print(request.user)



        if not request.user.is_authenticated:
            return HttpResponse('<script>alert("please login first.");history.back(-1);</script>')


        if len(dishes) == 0:
            return HttpResponse('<script>alert("You don\'t choose any dish.");history.back(-1);</script>')

        new_order = Order(user=request.user,
                          )
        new_order.save()
        new_order.orderId = new_order.id
        new_order.save()

        total = 0
        for i in range(len(dishes)):
            the_price = Dish.objects.get(name=dishes[i]).price
            total += the_price * int(numbers[i])
            new_orderDish = OrderDishes(order=new_order,
                                        dish=Dish.objects.get(name=dishes[i]),
                                        count=numbers[i],
                                        price=the_price,
                                        subtotal=the_price * int(numbers[i]),
                                        )
            new_orderDish.save()
        new_order.total = total
        new_order.save()

        return redirect(reverse('order:order_page', kwargs={'id': new_order.id}))


def order_page(request, id):
    try:
        the_order = Order.objects.get(id=id,status=0)
    except:
        the_order=Order.objects.get(id=id,status=1)
        context={'the_order':the_order}
        return render(request, 'success_page.html', context)

    the_order_dishes = OrderDishes.objects.filter(order=the_order)
    list = the_order_dishes
    search_dict = {'user': request.user, 'is_default': True}

    try:
        the_address = Address.objects.get(**search_dict)
    except Address.DoesNotExist:
        the_address = None

    context = {'list': list, 'the_order': the_order, 'the_address': the_address}
    return render(request, 'checkout.html', context)


def success_page(request,id):
    print(id)
    the_order = Order.objects.get(id=id)
    the_order.status=1
    the_order.address=Address.objects.get(user=the_order.user,is_default=True)
    the_order.save()
    context={'the_order':the_order}
    return render(request, 'success_page.html', context)
