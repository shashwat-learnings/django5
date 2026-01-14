from django.shortcuts import render
from django.core.cache import cache
import time


# Create your views here.
def course_view(request):
    mv=cache.get_or_set('movie', 'Django Movie Part 2', 30)  # Cache for 30 seconds
    # mv = cache.get('movie','has_expired_cache')
    # if mv == 'has_expired_cache':
    #     cache.set('movie', 'Django Movie', 30)  # Cache for 30 seconds
    #     mv = cache.get('movie')
    #     print("Cache Miss: Setting movie in cache.")
    return render(request, 'student/course.html', {'mv': mv})