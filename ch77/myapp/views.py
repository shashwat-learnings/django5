from django.shortcuts import render,HttpResponse
from .forms import ContactForm
from django.views import View

# Create your views here.

def myfunview1(request):
    return HttpResponse("This is my first function-based view.")

class MyClassBasedView1(View):
    def get(self, request):
        return HttpResponse("This is a GET request in a class-based view.")


def myfunview2(request):
    return HttpResponse("<h1>This is my second function-based view.</h1>")

class MyClassBasedView2(View):
    def get(self, request):
        return HttpResponse("<h1>This is a GET request in a class-based view.</h1>")

class MyClassBasedView3(View):
    name = "Sonam"
    def get(self, request):
        return HttpResponse(f"<h1>This is a GET request in a class-based view for {self.name}.</h1>")


def homefunview(request):
    return render(request, 'myapp/home.html')

class HomeClassBasedView(View):
    def get(self, request):
        return render(request, 'myapp/home.html')

def aboutfunview(request):
    context = {
        'name': 'John Doe',
        'age': 30,
        'email': ''}
    return render(request, 'myapp/about.html', context)

def contactfunview(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            print(f"Received contact form submission: Name={name}, Email={email}, Message={message}")
            return HttpResponse("Thank you for contacting us!")
    else:
        form = ContactForm()
        print("Contact form accessed via GET request.")
    return render(request, 'myapp/contact.html',{'form': form})

class ContactClassBasedView(View):
    def get(self, request):
        form = ContactForm()
        print("Contact form accessed via GET request.")
        return render(request, 'myapp/contact.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            print(f"Received contact form submission: Name={name}, Email={email}, Message={message}")
            return HttpResponse("Thank you for contacting us!")
        else:
            print("Contact form submission is invalid.")
            return render(request, 'myapp/contact.html', {'form': form})

def newsfunview(request,template_name):
    template_name = template_name
    context = {
        'info': f'This is news page for template: {template_name}'
    }
    return render(request, template_name, context)

# def newsfunview(request):
#     template_name = 'myapp/news.html'
#     context = {
#         'info': f'This is news page for template: {template_name}'
#     }
#     return render(request, template_name, context)
