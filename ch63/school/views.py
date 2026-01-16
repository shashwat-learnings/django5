from django.shortcuts import render

from datetime import date,time
from .models import Student

# Create your views here.

def home(request):
    # student = Student.objects.all()[10:20:2]  # Fetch students from index 10 to 19 with a step of 2
    student = Student.custom.all()  # Using custom manager to fetch students 
    # student = Student.custom.get_stu_roll_range(10, 20)  # Using custom manager to fetch students ordered by name
    return render(request, 'school/home.html', {"student": student})