from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.
def sync_view(request):
    print("This is a synchronous view.")
    return HttpResponse("Hello, this is a synchronous view!")

# Create your views here.
async def async_view(request):
    print("This is an asynchronous view.")
    return HttpResponse("Hello, this is an asynchronous view!")