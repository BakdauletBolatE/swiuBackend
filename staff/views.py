from django.shortcuts import render
from .models import Staff

# Create your views here.

def stuffDetailView(request,url):

    stuff = Staff.objects.get(slug=url)

    context = {
        'stuff':stuff,
    }

    return render(request,'stuff/stuffDetai.html',context)