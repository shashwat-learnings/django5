from django.urls import path
from student import views

urlpatterns = [
    path('course/', views.course, name='course'),
]