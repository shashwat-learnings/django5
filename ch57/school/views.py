from django.shortcuts import render
from .models import Student, Teacher

# Create your views here.

def home(request):
    # student = Student.objects.get(pk=1)
    # student = Student.objects.first()
    # student = Student.objects.order_by('-id').first()
    # student = Student.objects.last()
    # student = Student.objects.latest('pass_date')
    # student = Student.objects.latest('pass_date', 'id') # in case of tie, use id to decide
    # student = Student.objects.earliest('pass_date', 'id') # in case of tie, use id to decide
    # student = Student.objects.all().exists()

    # Student.objects.create(name="Alex", roll=105, city="Los Angeles", marks=88, pass_date="2023-05-20")
    # student = Student.objects.get(roll=105)
    # student,created  = Student.objects.get_or_create(name="Alex", roll=105, city="Los Angeles", marks=88, pass_date="2023-05-20")

    # Student.objects.filter(id=1).update(name='Rohit Sharma')
    # student= Student.objects.get(id=1)

    student = Student.objects.update_or_create(id=10, name='Anisa', defaults={'name': 'Anisa', 'roll':110, 'city':'Miami', 'marks':92, 'pass_date':'2023-06-15'})


    print(student)
    return render(request, 'school/home.html',{"student": student})