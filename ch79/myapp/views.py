from django.shortcuts import render
from django.views.generic.base import RedirectView

class MyRedirectView(RedirectView):
    url = '/home/'  # URL to redirect to
    query_string = True  # Optional: whether to include query parameters in the redirect 
    # pattern_name = 'homefunview'  # Optional: name of the URL pattern to redirect to

    def get_redirect_url(self, *args, **kwargs):
        # You can add custom logic here if needed
        print("Redirecting to home page...")
        # kwargs['id'] = 42  # Example of adding a parameter to the URL
        return super().get_redirect_url(*args, **kwargs)
    

