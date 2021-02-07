from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):

    years = Year.objects.all()

    return render(request,'library/index.html',{'years':years})

def bookList(request,url):
    year = Year.objects.get(slug=url)
    books = Book.objects.filter(year=year)

    context = {
        'year': year,
        'books': books,
    }
    return render(request,'library/book_list.html',context)

def bookDetail(request,url):

    book = Book.objects.get(slug=url)
    context = {
        'book': book,
    }
    return render(request,'library/book_detail.html',context)
