from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime,timedelta


# Create your views here.

def setcookie(request):
    response=render(request,'student/setcookie.html')
    response.set_cookie('token','phantom_django_123')
    response.set_cookie('pay_id','pay_456_xyz',max_age=10)

    return response

def getcookie(request):
    cookie=request.COOKIES
    pay_id=request.COOKIES.get('pay_id')
    response=render(request,'student/getcookie.html',{'cookie':cookie })
    return response

def delcookie(request):
    response=render(request,'student/delcookie.html')
    response.delete_cookie('pay_id')
    # response.delete_cookie('name')
    return response

def setsignedcookie(request):
    response=render(request,'student/setsignedcookie.html')
    response.set_signed_cookie('name','phantom',salt='my_salt_123',)
    return response

def getsignedcookie(request):
    name=request.get_signed_cookie('name',salt='my_salt_123',default='Guest')
    response=render(request,'student/getsignedcookie.html',{'cookie':name})
    return response