from django.shortcuts import render

# Create your views here.

def course(request):
    courses = [
        {'name': 'Mathematics', 'code': 'MATH101'},
        {'name': 'Physics', 'code': 'PHYS101'},
        {'name': 'Chemistry', 'code': 'CHEM101'},
    ]
    return render(request, 'student/course.html', {'courses': courses})