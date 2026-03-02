from django.http import JsonResponse
from django.shortcuts import render
from asgiref.sync import sync_to_async, async_to_sync
from .models import Student


# Create your views here.
def my_sync_function(x):
    return x*2

async def my_async_function1():
    result =await sync_to_async(my_sync_function)(10)
    print(f"Result from my_async_function1: {result}")

async def my_async_function(x):
    return x*2

def my_sync_function():
    result = async_to_sync(my_async_function)(10)
    print(f"Result from my_sync_function1: {result}")

# def get_student_data():
#     return list(Student.objects.filter(age__gt=1).values())


# async def get_student_data_async(request):
#     student_data = await sync_to_async(get_student_data)()
#     return JsonResponse({"students": student_data})

async def get_student_data_async(request):
    student_data = await sync_to_async(lambda: list(Student.objects.filter(age__gt=1).values()))()
    return JsonResponse({"students": student_data})   