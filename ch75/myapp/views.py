from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.
def home(request):
    students = Student.objects.all()
    for student in students:
        print(f"name: {student.name}, age: {student.age}, email: {student.email}")
    return render(request, 'myapp/home.html', {'students': students})

# Create your views here.
async def async_home(request):
    async for student in Student.objects.all():
        print(f"name: {student.name}, age: {student.age}, email: {student.email}")
    return render(request, 'myapp/home.html', {'students': 'students'})