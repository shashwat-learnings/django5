from django.urls import path
from . import views

urlpatterns = [
    path('funview1/', views.myfunview1, name='funview1'),
    path('classview1/', views.MyClassBasedView1.as_view(), name='classview1'),
    path('funview2/', views.myfunview2, name='funview2'),
    path('classview2/', views.MyClassBasedView2.as_view(), name='classview2'),
    path('classview3/', views.MyClassBasedView3.as_view(name='Rahual'), name='classview3'),

    path('home/', views.homefunview, name='home'),
    path('about/', views.aboutfunview, name='about'),
    path('contact/', views.contactfunview, name='contact'),
    path('news/', views.newsfunview,{'template_name': 'myapp/news.html'}, name='news'),
    path('new2/', views.newsfunview,{'template_name': 'myapp/new2.html'}, name='new2'),
]   