from django.urls import path
from . import views
from django.views.generic.base import TemplateView,RedirectView

urlpatterns = [
    path('', views.ContactFormView.as_view(), name='home'),

]   