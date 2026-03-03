from django.shortcuts import render
from django.views import View
from myapp.models import Student
from django.views.generic.detail import DetailView

class SingleStudentView(View):
    def get(self, request,pk):
        students = Student.objects.get(pk=pk)
        return render(request, 'myapp/home.html', {'students': students})
    

class SingleStudentDetailView(DetailView):
    model = Student  
    template_name = 'myapp/home.html' # template_name is optional, by default it will look for myapp/student_detail.html
    context_object_name = 'students' # context_object_name is optional, by default it will be object or student based on the model name
    
    # pk_url_kwarg = 'pk' # pk_url_kwarg is optional, by default it will be pk, if you want to use a different name for the primary key in the URL, you can set this attribute to the name of the URL parameter that contains the primary key. For example, if your URL pattern uses <int:id> instead of <int:pk>, you would set pk_url_kwarg = 'id'.
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_students'] = Student.objects.count()
        return context


    def get_template_names(self):
        if self.request.user.is_authenticated:
            template_name = 'myapp/home.html'
        else:
            template_name = self.template_name
        return [template_name]

    
        