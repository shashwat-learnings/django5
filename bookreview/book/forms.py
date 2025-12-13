from django import forms
from .models import Book    

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author','description','genre','isbn','publication_date']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter title'}),
            'author': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter author'}),
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 5, 'class': 'form-control','placeholder':'Enter description'}),
            'genre': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter genre'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter isbn'}),
            'publication_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control','placeholder':'Enter publication date'}),
        }
        