from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from myapp.models import Student
from django.views.generic.edit import FormView
from .forms import ContactForm


class ContactFormView(FormView):
    form_class = ContactForm  
    template_name = 'myapp/home.html' 
    initial = {'name': 'John Doe'}
    def form_valid(self, form):
        # Process the form data here (e.g., send an email, save to database, etc.)
        # You can access the form data using form.cleaned_data
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        
        # For demonstration purposes, we'll just print the data to the console
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Message: {message}")
        
        # After processing the form, you can redirect to a success page or render a response
        # return super().form_valid(form)
        return HttpResponse("Thank you for your message!")  # You can replace this with a redirect to a success page
    
    # success_url = '/'  # Redirect to the home page after successful form submission

    def form_invalid(self, form):
        # return super().form_invalid(form)
        return HttpResponse("Form is invalid. Please correct the errors.")

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_message'] = "Welcome to the contact form!"
        return context