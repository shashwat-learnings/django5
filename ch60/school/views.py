from django.shortcuts import render
from django.db.models import Q

from datetime import date,time
from .models import Student

# Create your views here.

def home(request):
    # student = Student.objects.filter(Q(id=2) & Q(roll=57)) # AND operation
    # student = Student.objects.filter(Q(id=2) | Q(roll=57)) # OR operation 
    # student = Student.objects.filter(~Q(id=2)) # NOT operation
    # student = Student.objects.filter(Q(marks__gt=50) & ~Q(roll__gt=50)) # Combined AND and NOT operation
    return render(request, 'school/home.html', {"student": student})