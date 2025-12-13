from django.urls import path
from book import views

urlpatterns = [
    path('book-list/', views.book_list, name='book-list'),
    path('book/new/', views.book_create, name='book-create'),
    path('book/<int:pk>/detail/', views.book_detail, name='book-detail'),
    path('book/<int:pk>/update/', views.book_update, name='book-update'),
]
 
