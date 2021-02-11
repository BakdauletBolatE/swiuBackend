from django.shortcuts import render
from .models import Staff
from faculties.models import PageCategory

# Create your views here.

def stuffDetailView(request,url):
    pageCats = PageCategory.objects.all()
    stuff = Staff.objects.get(slug=url)

    context = {
        'stuff':stuff,
        'pageCats':pageCats
    }

    return render(request,'stuff/stuffDetai.html',context)