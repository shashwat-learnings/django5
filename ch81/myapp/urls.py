from django.urls import path
from . import views
from django.views.generic.base import TemplateView,RedirectView

urlpatterns = [
    path('<int:pk>/', views.SingleStudentView.as_view(), name='home'),
    path('students/<int:pk>/', views.SingleStudentDetailView.as_view(), name='students'),

]   