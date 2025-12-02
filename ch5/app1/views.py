from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

##
def homepageslas(request):
    return HttpResponse('Hello  home page /')
def homepage(request):
    return HttpResponse('Hello home page')
def myfunction(request):
    return HttpResponse('Hello Django')