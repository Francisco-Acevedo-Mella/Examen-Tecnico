from django import forms
from django.db.models import fields
from app.models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title","author", "description"]
        labels = {
            "title" : "Titulo",
            "author" : "Autor",
            "description" : "Descripcion",
        }

widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            
        }



