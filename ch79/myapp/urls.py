from django.urls import path
from . import views
from django.views.generic.base import TemplateView,RedirectView

urlpatterns = [
    path('home/', TemplateView.as_view(template_name='myapp/home.html'), name='homefunview'),
    path('redirect/', RedirectView.as_view(url='/home/'), name='redirectview'),
    path('index/', views.MyRedirectView.as_view(), name='myredirectview'),
    path('index2/',RedirectView.as_view(pattern_name='home'), name='myredirectview'),

]   