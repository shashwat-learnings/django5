from django.shortcuts import render
from django.template.response import TemplateResponse

# Create your views here.

def home(request):
    print("I am in home view")
    return render(request, 'blog/home.html')


def math(request):
    print("I am in math view")
    a=10/0
    return render(request, 'blog/math.html', {'a':a})

def user(request):
    print("I am in user view")
    context = {'name':'John Doe'}
    return TemplateResponse(request, 'blog/user.html', context)
