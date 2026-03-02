from django.shortcuts import render
from django.views import View
from myapp.models import Student
from django.views.generic.list import ListView

class AllStudentsView(View):
    def get(self, request):
        students = Student.objects.all()
        return render(request, 'myapp/home.html', {'students': students})
    

class AllStudentsListView(ListView):
    model = Student
    # queryset = Student.objects.all() # queryset is optional, by default it will be Student.objects.all() based on the model name
    template_name = 'myapp/home.html' # template_name is optional, by default it will look for myapp/student_list.html
    context_object_name = 'students' # context_object_name is optional, by default it will be object_list or student_list based on the model name
    # template_name_suffix = '_list' # template_name_suffix is optional, by default it will be _list based on the model name
    # ordering = ['name'] # ordering is optional, by default it will be ordered by id
    # paginate_by = 10 # paginate_by is optional, by default it will not paginate
    
    # def get_queryset(self):
    #     return Student.objects.filter(age__gte=18)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['total_students'] = Student.objects.count()
    #     return context


    def get_template_names(self):
        if self.request.user.is_authenticated:
            template_name = 'myapp/home.html'
        else:
            template_name = self.template_name
        return [template_name]

    
        