from django.shortcuts import render

from datetime import date,time
from .models import Student

# Create your views here.

def home(request):
    # student = Student.objects.all()[:5]  # Fetch first 5 students
    # student = Student.objects.all()[5:10]  # Fetch students from index 5 to 9
    # student = Student.objects.all()[::-1]  # Fetch all students in reverse order
    # student = Student.objects.all()[:10:2]  # Fetch students till index 10 to end with a step of 2
    student = Student.objects.all()[10:20:2]  # Fetch students from index 10 to 19 with a step of 2

    return render(request, 'school/home.html', {"student": student})