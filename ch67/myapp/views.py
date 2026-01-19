from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Page, Post, Song


# Create your views here.
def home(request):
    return render(request,'myapp/home.html')

def show_user_data(request):
    data1 = User.objects.all()
    data2 = User.objects.filter(email = "raj@example.com")
    data3 = User.objects.filter(page__pcat='Tech')
    data4 = User.objects.filter(post__ptpublished='2024-12-13')
    data5 = User.objects.filter(song__sduration=4)
    return render(request,'myapp/user.html',)


def show_page_data(request):
    data1 = Page.objects.all()
    data2 = Page.objects.filter(pcat = 'tech')
    data3 = Page.objects.filter(ppublished = '2024-12-13')
    data4 = Page.objects.filter(user__email = 'raj@example.com')

    return render(request,'myapp/page.html')

def show_post_data(request):
    data1 = Post.objects.all()
    data2 = Post.objects.filter(ptpublished = '2024-12-13')
    data3 = Post.objects.filter(user__email = 'raj@example.com')
    return render(request,'myapp/post.html')

def show_song_data(request):
    data1 = Song.objects.all()
    data2 = Song.objects.filter(sduration = 4)
    data3 = Song.objects.filter(user__email = 'raj@example.com')
    return render(request,'myapp/song.html')