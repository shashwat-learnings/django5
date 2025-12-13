from django.urls import path, register_converter
from course.views import learn_django, learn_fast, home,success,profile
from course.converters import FourDigitYearConverter

register_converter(FourDigitYearConverter,'yyyy')
urlpatterns = [
    path('dj/', learn_django, name='learn_django'),
    path('fst/', learn_fast, name='learn_fast'),
    path('success/',success,name='success'),
    # dynamic urls
    path('profile/<int:my_id>',profile,name='profile'),

    # custom path generater
    # path('custom/profile/<yyyy:my_id>',profile,name='profile'),

    path('', home, name='home'),

]
