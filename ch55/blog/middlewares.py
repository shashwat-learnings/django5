from django.shortcuts import render
from django.http import HttpResponse

def my_fun_middleware(get_response):
    # One-time configuration and initialization.
    print("Middleware initialized")
    def middleware(request): #function name can be anything .e.g. middleware_func or my_funcc
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("Before view")

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        print("After view")

        return response

    return middleware

class MyClassMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
        print("Class-based Middleware initialized")

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("Before view in class-based middleware")

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        print("After view in class-based middleware")

        return response
    
class MyProcessViewMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
        print("Process View Middleware initialized")

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("Before view in process view middleware")

        response = self.get_response(request)

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Code to be executed just before the view is called.
        print("Inside process_view method")
        return None # Returning None allows the view to be called
    
class MyExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
        print("Exception Middleware initialized")

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("Before view in exception middleware")

        response = self.get_response(request)

        return response

    def process_exception(self, request, exception):
        # Code to be executed if an exception occurs in the view.
        print(f"Exception caught in middleware: {exception}")
        msg=exception
        class_name = exception.__class__.__name__
        print(f"Exception class name: {class_name}")
        print(f"Exception message: {msg}")
        # return HttpResponse(f"Exception handled in middleware: {msg}")
       
        # return render(request, 'blog/exception.html', {'exception': msg})
        return None # Returning None allows default exception handling
    

class MyTemplateResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
        print("Template Response Middleware initialized")

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("Before view in template response middleware")

        response = self.get_response(request)

        return response

    def process_template_response(self, request, response):
        # Code to be executed just after the view has
        # finished executing, if the response instance
        # has a TemplateResponse() method.
        print("Inside process_template_response method")
        response.context_data['name'] = 'Data added by TemplateResponse Middleware'
        return response