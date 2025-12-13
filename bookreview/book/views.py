from django.shortcuts import render,redirect
from book.models import Book
from book.forms import BookForm 
from django.contrib import messages


def book_list(request):
    books = Book.objects.all()
    genre = request.GET.get('genre')
    if genre:
        books = books.filter(genre=genre)
    context = {'books': books, 'genres': Book.GENRE_CHOICES}
    
    return render(request, 'book/book_list.html', context)


def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book added successfully.')
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'book/book_create.html', {'form': form})


def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'book/book_detail.html', {'book': book})

def book_update(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'book/book_update.html', {'form': form})
