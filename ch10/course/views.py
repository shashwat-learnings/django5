from django.shortcuts import render
from django.http import HttpResponse
from course.models import Profile
from course.forms import Registration
# Create your views here.


def learn_django(request):
    # render(request, template_name, context=dict,content_type=MIME_TYPE, status=None, using=None)
    return render(request, 'course/django.html',context= {'cname':'Django Framework','description':'Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.','name':['Models','Views','Templates (MVT) Architecture','ORM (Object-Relational Mapping)','Admin Interface','Security Features','Scalability and Versatility']})

def learn_fast(request):
    form = Registration()
    # render(request, template_name, context=dict,content_type=MIME_TYPE, status=None, using=None)
    return render(request, 'course/fastapi.html',{'form':form})

def home(request):
    # render(request, template_name, context=dict,content_type=MIME_TYPE, status=None, using=None)
    students=Profile.objects.all()
    print(students)
    return render(request, 'course/home.html',{'students':students})