from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from user import forms
from user.models import User, Address
from order.models import Order, OrderDishes
# from itsdangerous import TimedJSONWebSignatureSerializer, SignatureExpired
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def register_action(request):
    return render(request, 'register.html')


# def register_action(request):
#     context = {}
#     if request.method == 'GET':
#         context['form'] = forms.RegistrationForm()
#         return render(request, 'register.html', context)
#     if request.method == 'POST':
#         form = forms.RegistrationForm(request.POST)
#         context['form'] = form
#
#         if not form.is_valid():
#             return render(request, 'register.html', context)
#
#
#         new_user = User.objects.create_user(username=form.cleaned_data['username'],
#                                             password=form.cleaned_data['password'],
#                                             email=form.cleaned_data['email'],)
#         new_user.is_active=1
#         new_user.save()
#         new_user = authenticate(username=form.cleaned_data['username'],
#                                 password=form.cleaned_data['password'])
#
#         # login(request, new_user)
#
#         return redirect(reverse('home'))
# def register_action(request):
#     context = {}
#     if request.method == 'GET':
#         context['form'] = forms.RegistrationForm()
#         return render(request, 'register.html', context)
#     if request.method == 'POST':
#         form = forms.RegistrationForm(request.POST)
#         context['form'] = form
#
#         if not form.is_valid():
#             return render(request, 'register.html', context)
#
#         new_user = User.objects.create_user(username=form.cleaned_data['username'],
#                                             password=form.cleaned_data['password'],
#                                             email=form.cleaned_data['email'], )
#         new_user.is_active = 0
#         new_user.save()
#
#         # send the active e-mail containing active link
#         # contains the user's id but should be encoded use package itsdangerous
#
#         #use the class secret_key and the expired time millisec
#         ss = TimedJSONWebSignatureSerializer(settings.SECRET_KEY, 3600)
#         info = {'confirm': new_user.id}
#
#         ##encode the info
#         token = ss.dumps(info)
#         token = token.decode()
#
#         print(token)
#         ##send the e-mail
#         subject = 'team42 restaurant active message'
#         # sender = settings.EMAIL_FROM
#         sender = 'team42<jiahengz@andrew.cmu.edu>'
#         message = ''
#         html_message = '<h1>Hello %s,welcome to become our restaurant\'s new member!</h1>Please click the link below to active the new account<br>' \
#                        '<a href="http://127.0.0.1:8000/user/active/%s">http://127.0.0.1:8000/user/active/%s</a>' % (
#                        new_user.username, token, token)
#         receive = [new_user.email]
#
#         send_mail(subject, message, sender, receive, html_message=html_message)
#
#         return redirect(reverse('dish:home'))
#
#
# def active_action(request, token):
#     ss = TimedJSONWebSignatureSerializer(settings.SECRET_KEY, 3600)
#     try:
#         # decode the token
#         info = ss.loads(token)
#         user_id = info['confirm']
#
#         # active the user
#         user = User.objects.get(id=user_id)
#         user.is_active = 1
#         user.fix_time = timezone.now()
#         user.save()
#
#         login(request, user)
#         return redirect(reverse('dish:home'))
#     except SignatureExpired as e:
#         return HttpResponse('the active link has expired')




def register_action(request):
    context = {}
    if request.method == 'GET':
        context['form'] = forms.RegistrationForm()
        return render(request, 'register.html', context)
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        context['form'] = form

        if not form.is_valid():
            return render(request, 'register.html', context)

        new_user = User.objects.create_user(username=form.cleaned_data['username'],
                                            password=form.cleaned_data['password'],
                                            email=form.cleaned_data['email'], )
        new_user.is_active = 0
        new_user.save()

        token = default_token_generator.make_token(new_user)

        email_body = """
        Hello new user,welcome to become our restaurant\'s new member! Please click the link below to active the new account

          http://{host}{path}
        """.format(host=request.get_host(),
                   path=reverse('user:active', args=(new_user.username, token)))

        send_mail(subject="team42 restaurant active message",
                  message=email_body,
                  from_email="team42<jiahengz@andrew.cmu.edu>",
                  recipient_list=[new_user.email])


        return redirect(reverse('dish:home'))


def active_action(request, username,token):
    user = get_object_or_404(User, username=username)

    # Send 404 error if token is invalid
    if not default_token_generator.check_token(user, token):
        raise Http404

    # Otherwise token was valid, activate the user.
    user.is_active = 1
    user.fix_time = timezone.now()
    user.save()
    login(request, user)
    return redirect(reverse('dish:home'))

    # ss = TimedJSONWebSignatureSerializer(settings.SECRET_KEY, 3600)
    # try:
    #     # decode the token
    #     info = ss.loads(token)
    #     user_id = info['confirm']
    #
    #     # active the user
    #     user = User.objects.get(id=user_id)
    #     user.is_active = 1
    #     user.fix_time = timezone.now()
    #     user.save()
    #
    #     login(request, user)
    #     return redirect(reverse('dish:home'))
    # except SignatureExpired as e:
    #     return HttpResponse('the active link has expired')





def login_action(request):
    context = {}
    if request.method == 'GET':
        if 'username' in request.COOKIES:
            username = request.COOKIES.get('username')
            checked = 'checked'
        else:
            username = ''
            checked = ''
        form = forms.LoginForm()
        form.fields['username'].initial = username
        context['form'] = form
        context['checked'] = checked
        return render(request, 'login.html', context)

    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        context['form'] = form

        if not form.is_valid():
            return render(request, 'login.html', context)

        new_user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])

        login(request, new_user)

        response = redirect(reverse('dish:home'))
        # judge remember tag is click

        remember = request.POST.get('remember')

        if remember == 'on':
            response.set_cookie('username', new_user.username, max_age=7 * 24 * 3600)
        else:
            response.delete_cookie('username')

        return response


def logout_action(request):
    logout(request)
    return redirect(reverse('user:login'))


def centre_information(request):
    # address = Address.objects.get_default_address(user)
    if request.method == 'GET':
        user = request.user
        try:
            address = Address.objects.get(user=user, is_default=True)

        except Address.DoesNotExist:
            address = None
        return render(request, 'centre_information.html', {'address': address})

    # if request.method == 'GET':
    #     user = request.user
    #     address = Address.objects.get(user=user,is_default=True)
    #
    #     return render(request, 'centre_information.html', {'address': address})


def centre_order_list(request):
    if request.method == 'GET':
        user = request.user
        orders = Order.objects.filter(user=user)

    return render(request, 'centre_order_list.html', {'orders': orders, 'user': user})


def centre_order_detail(request, id):
    if request.method == 'GET':
        order = Order.objects.get(id=id)
        order_dishes = OrderDishes.objects.filter(order=order)
        order.total = 0
        for dish in order_dishes:
            subtotal = dish.count * dish.price
            dish.subtotal = subtotal
            order.total += subtotal

    return render(request, 'centre_order_detail.html', {'order': order, 'dishes': order_dishes})


def centre_address(request):
    if request.method == 'GET':
        user = request.user
        try:
            address = Address.objects.get(user=user, is_default=True)

        except Address.DoesNotExist:
            address = None
        return render(request, 'centre_address.html', {'address': address})
    if request.method == 'POST':
        # print('****')
        receiver = request.POST.get('receiver')
        # print(receiver)
        addr = request.POST.get('address')
        # print(addr)
        zip_code = request.POST.get('zip_code')
        # print(zip_code)
        phone = request.POST.get('phone')
        # print(phone)

        if not all([receiver, addr, phone]):
            print('55555')
            return HttpResponse('<script>alert("You don\'t write a whole address.");history.back(-1);</script>')

        user = request.user
        try:
            address = Address.objects.get(user=user, is_default=True)
            address.is_default = False
            address.save()
        except Address.DoesNotExist:
            address = None

        # if address:
        #     is_default = False
        # else:
        #     is_default = True
        try:
            int(zip_code)
        except:
            return HttpResponse('<script>alert("You don\'t write zip code as a number.");history.back(-1);</script>')

        try:
            int(phone)
        except:
            return HttpResponse('<script>alert("You don\'t write phone as a number.");history.back(-1);</script>')

        Address.objects.create(user=user,
                               receiver=receiver,
                               addr=addr,
                               zip_code=zip_code,
                               phone=phone,
                               is_default=True)

        # user = request.user
        # print(Address.objects.all())
        # try:
        #     address = Address.objects.get(user=user, is_default=True)
        #
        # except Address.DoesNotExist:
        #     address = None
        # return render(request, 'centre_address.html', {'address': address})

        return redirect(reverse('user:centre_address'))


def other_address(request,id):
    if request.method=='GET':
        user = request.user
        try:
            address = Address.objects.get(user=user,is_default=True)
        except Address.DoesNotExist:
            address = None
        return render(request, 'other_address.html', {'address':address,'order_id':id})

    if request.method == 'POST':
        # print('****')
        receiver = request.POST.get('receiver')
        # print(receiver)
        addr = request.POST.get('address')
        # print(addr)
        zip_code = request.POST.get('zip_code')
        # print(zip_code)
        phone = request.POST.get('phone')
        # print(phone)

        if not all([receiver, addr, phone]):
            return HttpResponse('<script>alert("You don\'t write a whole address.");history.back(-1);</script>')

        user = request.user
        try:
            address = Address.objects.get(user=user,is_default=True)
            address.is_default=False
            address.save()
        except Address.DoesNotExist:
            address = None

        # if address:
        #     is_default = False
        # else:
        #     is_default = True


        try:
            int(zip_code)
        except:
            return HttpResponse('<script>alert("You don\'t write zip code as a number.");history.back(-1);</script>')

        try:
            int(phone)
        except:
            return HttpResponse('<script>alert("You don\'t write phone as a number.");history.back(-1);</script>')

        Address.objects.create(user=user,
                               receiver = receiver,
                               addr = addr,
                               zip_code = zip_code,
                               phone = phone,
                               is_default = True)

        # user = request.user
        # print(Address.objects.all())
        # try:
        #     address = Address.objects.get(user=user, is_default=True)
        #
        # except Address.DoesNotExist:
        #     address = None
        # return render(request, 'centre_address.html', {'address': address})

        return redirect(reverse('order:order_page',kwargs={'id': id}))




