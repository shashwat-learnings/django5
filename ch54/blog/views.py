from django.http import HttpResponse
from django.shortcuts import render
from blog.signals import notification

def home(request):
    notification.send(sender=None,request=request,user=["SHASHWAT"], message="Home page accessed")
    return HttpResponse("Welcome to the Blog Home Page!")

# Create your views here.
