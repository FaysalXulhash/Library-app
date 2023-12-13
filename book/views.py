from django.shortcuts import render, redirect
from .forms import BookCreate
from .models import Book
# Create your views here.

def createBook(request):
    if request.method == 'POST':
        form = BookCreate(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view-book')
    else:
        form = BookCreate()
    return render(request, 'book/createbook.html', {'form':form})
def successpage(request):
    return render (request, 'book/success.html')
def viewBook(request):
    books = Book.objects.all()
    ordering = ['-id']
    return render (request, 'book/viewbook.html', {'books':books})


def deleteBook(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('view-book')

def updatebook(request, id):
    queryset = Book.objects.get(id=id)
    if request.method == 'POST':
        form = BookCreate(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('view-book')
    else:
        queryset = Book.objects.get(id=id)
        form = BookCreate(instance=queryset)
    return render(request, 'book/updatebook.html', {'form':form} )