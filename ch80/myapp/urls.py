from django.urls import path
from . import views
from django.views.generic.base import TemplateView,RedirectView

urlpatterns = [
    path('', views.AllStudentsView.as_view(), name='home'),
    path('students/', views.AllStudentsListView.as_view(), name='students'),

]   