from django.urls import path
from course.views import learn_django, learn_fast, home,success

urlpatterns = [
    path('dj/', learn_django, name='learn_django'),
    path('fst/', learn_fast, name='learn_fast'),
    path('fst/', learn_fast, name='learn_fast'),
    path('success/',success,name='success'),
    path('', home, name='home'),

]
