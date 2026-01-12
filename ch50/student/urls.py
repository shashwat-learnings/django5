from django.urls import path
from student import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('course/', views.course, name='course'),
    path('result/', cache_page(timeout=60)(views.results), name='result'),
    path('', views.home, name='home'),
]