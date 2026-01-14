from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home),
    path('math/', views.math),
    path('user/', views.user),
]