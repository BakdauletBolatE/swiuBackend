from django.http.response import HttpResponse
from django.shortcuts import render
from .models import *
from faculties.models import PageCategory
import json
# Create your views here.
def libindex(request):

    years = Year.objects.all()
    pageCats = PageCategory.objects.all()
    internatiolization = PageCategory.objects.get(id=3)
    context = {
        'years':years,
        'pageCats':pageCats,
        'internatiolization':internatiolization
    }

    return render(request,'library/index.html',context)

def teachStaff(request):

    years = Year.objects.all().order_by('-year')
    pageCats = PageCategory.objects.all()
    internatiolization = PageCategory.objects.get(id=3)
    context = {
        'years':years,
        'pageCats':pageCats,
        'internatiolization':internatiolization
    }

    return render(request,'library/teacshingStaff.html',context)

def bookList(request,url):
    year = Year.objects.get(slug=url)
    books = Book.objects.filter(year=year)
    pageCats = PageCategory.objects.all()
    internatiolization = PageCategory.objects.get(id=3)

    context = {
        'year': year,
        'books': books,
        'pageCats':pageCats,
        'internatiolization':internatiolization
    }
    return render(request,'library/book_list.html',context)

def bookDetail(request,url):
    pageCats = PageCategory.objects.all()
    book = Book.objects.get(slug=url)
    rec = []
    try:
        recItem = Book.objects.get(id=book.id+1)
        rec.append(recItem)
    except Book.DoesNotExist:
        recItem = Book.objects.get(id=book.id-1)
        rec.append(recItem)
    
    try:
        recItem2 = Book.objects.get(id=book.id+2)
        rec.append(recItem2)
    except Book.DoesNotExist:
        recItem2 = Book.objects.get(id=book.id-2)
        rec.append(recItem2)

    internatiolization = PageCategory.objects.get(id=3)
    context = {
        'book': book,
        'pageCats':pageCats,
        'internatiolization':internatiolization,
        'recs':rec
    }
    return render(request,'library/book_detail.html',context)



def dlearning(request):

    pageCats = PageCategory.objects.all()
    internatiolization = PageCategory.objects.get(id=3)
    context = {
        'pageCats':pageCats,
        'internatiolization':internatiolization
    }
    return render(request,'distancelearning/isudo.html',context)



def saveRegistration(request):

    if request.method == "POST":
        data = json.load(request.body)
   

        name = data['name']
        phone = data['phone']
        group = data['group']
        course = data['course']

        reg = Registration.objects.create(
            name=name,
            phone=phone,
            group=group,
            course=course
        )
        reg.save()

        return HttpResponse("YES")

