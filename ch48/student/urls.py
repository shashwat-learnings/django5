from django.urls import path
from student import views

urlpatterns = [
    path('set/', views.setsession, name='setsession'),
    path('get/', views.getsession, name='getsession'),
    path('clear/', views.sessionclear, name='sessionclear'),
]