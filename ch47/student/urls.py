from django.urls import path
from student import views

urlpatterns = [
    path('set/', views.setsession, name='setsession'),
    path('get/', views.getsession, name='getsession'),
    path('del/', views.deletesession, name='deletesession'),
    path('flush/', views.flushsession, name='flushsession'),
    path('inview/', views.sessionmethodsinview, name='sessionmethodsinview'),
    path('intemplate/', views.sessionmethodsintemplate, name='sessionmethodsintemplate'),
    path('clear/', views.sessionclear, name='sessionclear'),
    path('settest/', views.settestcookie, name='settestcookie'),
    path('checktest/', views.checktestcookie, name='checktestcookie'),
    path('deltest/', views.deltestcookie, name='deltestcookie'),
]