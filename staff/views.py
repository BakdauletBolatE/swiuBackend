from django.shortcuts import render
from .models import Staff
from faculties.models import PageCategory

# Create your views here.

def stuffDetailView(request,url):
    pageCats = PageCategory.objects.all()
    stuff = Staff.objects.get(slug=url)
    internatiolization = PageCategory.objects.get(id=3)

    context = {
        'stuff':stuff,
        'pageCats':pageCats,
        'internatiolization':internatiolization
    }

    return render(request,'stuff/stuffDetai.html',context)