from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import HttpResponse
from .forms import LoginForm, UserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from .models import Product, Vip_reorder, Vip_aisle, Order_dow, Product_middle, Product_small
import json

def main_page(request):
    products = Product.objects.all()
    return render(request, 'shopapp/index.html', {'products':products})



# def signup(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             new_user = User.objects.create_user(**form.cleaned_data)
#             login(request, new_user)
#             return redirect('index')
#         else:
#             form = UserForm()
#             return render(request, 'shopapp/adduser.html', {'form':form})

def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('../')
        else:
            return HttpResponse('아이디 또는 비밀번호가 올바르지 않습니다')
    else:
        form = LoginForm()
        return render(request, 'shopapp/login.html', {'form':form})

def signout(request):
    logout(request)
    return redirect('../')

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('../')
        else:
            return HttpResponse('사용자명이 이미 존재합니다.')
    else:
        form = UserForm()
        return render(request, 'shopapp/adduser.html', {'form': form})

# def detail_middle(request):
#     middle_lists=Product_middle.objects.filter(department_id=5)
#     return render(request, 'shopapp/middle_detail.html', {'middle_lists':middle_lists})#'departments':departments

def detail_middle(request, a):
    middle_lists=Product.objects.filter(department_id=a)
    return render(request, 'shopapp/middle_detail.html', {'middle_lists':middle_lists})#'departments':departments

def detail_middle_five(request, a, aisle_id):
    detail_lists=Product.objects.filter(aisle_id=aisle_id)
    # detail_lists=Product_small.objects.filter(aisle_id=5)
    return render(request, 'shopapp/small_detail.html', {'detail_lists':detail_lists})

def chart_list(request):
    return render(request, 'shopapp/chart_list.html', {})


def chart_page(request):
    return render_to_response('shopapp/vipreorderchart.html')

def get_data(request):
    department=[]
    reordered=[]

    values = Vip_reorder.objects.all()
    for value in values:
        department.append(value.department)
        reordered.append(value.reordered)
    
    data = {
        'columns' : [
            department,
            reordered
        ]
    }
    return HttpResponse(json.dumps(data), content_type='application/json')

def vip_aisle_page(request):
    return render_to_response('shopapp/vipaisle.html')

def get_aisle(request):
    aisle=[]
    ratio=[]

    values = Vip_aisle.objects.all()
    for value in values:
        aisle.append(value.aisle)
        ratio.append(value.ratio)
    
    data = {
        'columns' : [
            aisle,
            ratio
        ]
    }
    return HttpResponse(json.dumps(data), content_type='application/json')

def order_dow_page(request):
    return render_to_response('shopapp/orderdow.html')

def get_dow(request):
    hours=[]
    sat=[]
    sun=[]
    mon=[]
    tues=[]
    wed=[]
    thrs=[]
    fri=[]

    for i in range(0, 25):
        hours.append(i)

    values = Order_dow.objects.all()
    for value in values:
        sat.append(value.Sat)
        sun.append(value.Sun)
        mon.append(value.Mon)
        tues.append(value.Tues)
        wed.append(value.Wed)
        thrs.append(value.Thrs)
        fri.append(value.Fri)
    
    data = {
        'columns' : [
            hours,
            sat,
            sun,
            mon,
            tues,
            wed,
            thrs,
            fri
        ]
    }
    return HttpResponse(json.dumps(data), content_type='application/json')