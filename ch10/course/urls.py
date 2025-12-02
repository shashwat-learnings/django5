from django.urls import path
from course.views import learn_django, learn_fast, home

urlpatterns = [
    path('dj/', learn_django, name='learn_django'),
    path('fst/', learn_fast, name='learn_fast'),
    path('', home, name='home'),

]
