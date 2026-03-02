from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('home/', TemplateView.as_view(template_name='myapp/home.html'), name='homefunview'),
    path('home3/<int:id>/', TemplateView.as_view(template_name='myapp/home.html'), name='homefunview'), # This is for dynamic URL pattern with an integer parameter 'id', the id can be accessed in the template using {{ id }}

    path('home2/', views.HomeView.as_view(extra_context={'name': 'Shashwat', 'title': 'Home Page'}), name='homeclassview'),
]   