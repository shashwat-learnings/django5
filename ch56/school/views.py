from django.shortcuts import render
from .models import Student, Teacher

# Create your views here.

def home(request):
    # all_data = Student.objects.all()
    # all_data = Student.objects.filter(city='New York')
    # all_data = Student.objects.exclude(city='New York')
    # all_data = Student.objects.order_by('-marks')
    # all_data = Student.objects.order_by('name')
    # all_data = Student.objects.order_by('name').reverse()
    # all_data = Student.objects.order_by('name')[0:5]
    # all_data = Student.objects.order_by('?') # random order
    # all_data = Student.objects.values('name', 'marks')
    # all_data = Student.objects.raw('SELECT * FROM school_student WHERE marks > 80')

    # all_data = Student.objects.values() # get all fields in dict format
    # all_data = Student.objects.values_list() # get all fields in tuple format
    # all_data = Student.objects.values_list('name', 'marks') # get specific fields
    # all_data = Student.objects.values_list('name', 'marks', named=True) # get specific fields as namedtuple
    # all_data = Student.objects.values('name', 'marks', 'city').order_by('-marks')


    qs1 = Student.objects.values_list('id', 'name', named=True)
    qs2 = Teacher.objects.values_list('id', 'name', named=True)


    # all_data = Student.objects.filter(name = "rohit") & Student.objects.filter(marks__gte = 80)
    # or
    # all_data = Student.objects.filter(name = "Shashwat", marks__gte = 80)

    # all_data = Student.objects.filter(name = "rohit") | Student.objects.filter(marks__gte = 80)


    # all_data = qs2.union(qs1)
    # all_data = qs2.union(qs1, all=True) # to include duplicates

    # all_data = qs2.intersection(qs1)
    # all_data = qs2.difference(qs1)

    print(all_data)
    print()



    # print("SQL Query:", all_data.query) # to see the actual SQL query being executed
    return render(request, 'school/home.html',{"all_data": all_data})