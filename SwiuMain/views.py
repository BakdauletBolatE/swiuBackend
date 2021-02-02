from django.shortcuts import render
from faculties.models import Facult
from staff.models import Staff
from news.models import Quote

def index(request):
    quotes = Quote.objects.all()[:3]
    context = {
        'quotes':quotes,
    }
    return render(request,'Main/index.html',context)

def aboutUs(request):
    intarnationalStaff = Staff.objects.filter(staffCat_id=1)

    context = {
        'intarnationalStaff':intarnationalStaff,
    }
    return render(request,'Main/pages/about-us.html', context)

def facultView(request):

    facults = Facult.objects.all()
    context = {
        'facults':facults,
    }
    return render(request,'facult/index.html',context)