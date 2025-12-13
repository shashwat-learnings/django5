from django.contrib import admin
from book.models import Book

# Register your models here.

@admin.register(Book)
class BookAdminn(admin.ModelAdmin):
    little_display = ('title','author','isbn')