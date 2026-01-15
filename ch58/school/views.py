from django.shortcuts import render
from datetime import date,time

from ch48 import student
from .models import Student

# Create your views here.

def home(request):
    # student = Student.objects.all()
    # student = Student.objects.filter(name__exact="rohit") # case sensitive
    # student = Student.objects.filter(name__iexact="rohit")  # case insensitive
    # student = Student.objects.filter(name__contains="ro")  # case sensitive
    # student = Student.objects.filter(name__icontains="RO")  # case insensitive
    # student = Student.objects.filter(id__in=[1, 3, 7]) #  id in list
    # student = Student.objects.filter(admission_date__year=2024)
    # student = Student.objects.filter(marks__gt=75)  # marks greater than 75
    # student = Student.objects.filter(marks__gte=75)  # marks greater than equal to 75
    # student = Student.objects.filter(marks__lt=75)  # marks less than 75
    # student = Student.objects.filter(marks__lte=75)  # marks less than equal to 75
    # student = Student.objects.filter(name__startswith="r")  # name starts with r
    # student = Student.objects.filter(name__istartswith="R")  # name starts with r case insensitive
    # student = Student.objects.filter(name__endswith="t")  # name ends with t
    # student = Student.objects.filter(name__iendswith="T")  # name ends with t case insensitive
    # student = Student.objects.filter(marks__range=(65, 80))  # marks between 65 and 80 inclusive  
    # student = Student.objects.filter(admission_date__year__gt=2022)  # admission year greater than 2022
    # student = Student.objects.filter(admission_date__year__lt=2023)  # admission year less than 2023
    # student = Student.objects.filter(admission_date__date=date(2023,8,15))  # admission date is 15th August 2023
    # student = Student.objects.filter(admission_date__year=2023, admission_date__month=8)  # admission in August 2023
    # student = Student.objects.filter(name__regex=r'^[rR].*t$')  # name starts with r or R and ends with t   
    # student = Student.objects.filter(name__iregex=r'^[rR].*T$')  # name starts with r or R and ends with t case insensitive
    # student = Student.objects.filter(pass_date__range=('2023-01-01', '2024-12-31'))  # pass_date between two dates



    print(student)
    return render(request, 'school/home.html', {"student": student})