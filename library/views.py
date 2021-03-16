from django.shortcuts import render
from .models import *
from faculties.models import PageCategory
# Create your views here.

def libindex(request):

    years = Year.objects.all()
    pageCats = PageCategory.objects.all()

    context = {
        'years':years,
        'pageCats':pageCats
    }

    return render(request,'library/index.html',context)

def bookList(request,url):
    year = Year.objects.get(slug=url)
    books = Book.objects.filter(year=year)
    pageCats = PageCategory.objects.all()

    context = {
        'year': year,
        'books': books,
        'pageCats':pageCats
    }
    return render(request,'library/book_list.html',context)

def bookDetail(request,url):
    pageCats = PageCategory.objects.all()
    book = Book.objects.get(slug=url)
    context = {
        'book': book,
        'pageCats':pageCats
    }
    return render(request,'library/book_detail.html',context)



def dlearning(request):

    pageCats = PageCategory.objects.all()
    context = {
        'pageCats':pageCats
    }
    return render(request,'distancelearning/isudo.html',context)

