from django.shortcuts import render
from django.views.decorators.cache import cache_page

# Create your views here.

def home(request):
    return render(request, 'student/home.html')


@cache_page(timeout=60)  # Cache this view for 1 minutes
def course(request):
    courses = [
        {'name': 'Mathematics', 'code': 'MATH101'},
        {'name': 'Physics', 'code': 'PHYS101'},
        {'name': 'Chemistry', 'code': 'CHEM101'},
    ]
    return render(request, 'student/course.html', {'courses': courses})

def results(request):
    results = [
        {'student': 'Alice', 'course': 'MATH101', 'grade': 'A'},
        {'student': 'Bob', 'course': 'PHYS101', 'grade': 'B+'},
        {'student': 'Charlie', 'course': 'CHEM101', 'grade': 'A-'},
    ]
    return render(request, 'student/result.html', {'results': results})