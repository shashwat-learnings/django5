from django.shortcuts import render
from django.db.models import Avg, Count, Max, Min, Sum

from datetime import date,time
from .models import Student

# Create your views here.

def home(request):
    student = Student.objects.all()
    # average = student.aggregate(Avg('marks')) # to calculate average marks of all students
    average = student.aggregate(Avg('marks'), Min('marks'), Max('marks'), Sum('marks'), Count('marks'))
    print(average)
    return render(request, 'school/home.html', {"student": average})