from django.shortcuts import render, redirect
from django.contrib import messages
from app.forms import BookForm
from app.models import Book
import bcrypt

def index(request):
    #POST

    
    books = Book.objects.all()
    
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()            
            messages.success(request, "Libro agregado correctamente")
            return redirect('/')
        else:
            messages.error(request, "Formulario procesado con errroes.")
            return render(request, 'app/index.html', {'form':form, "books" : books})
        
    else:
        #GET    
        context = {
            "form" : BookForm(),
            "books" : books
        }
    return render(request, 'app/index.html', context)










