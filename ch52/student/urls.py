from django.urls import path

from student.views import course_view

urlpatterns = [
    path('course/', course_view, name='course'),
]