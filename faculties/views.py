from django.shortcuts import render
from .models import Facult
from departments.models import Department
from .models import PageCategory

# Create your views here.

def facultView(request):

    facults = Facult.objects.all()
    pageCats = PageCategory.objects.all()
    internatiolization = PageCategory.objects.get(id=3)
    context = {
        'facults':facults,
        'pageCats':pageCats,
        'internatiolization':internatiolization
    }
    return render(request,'facult/index.html',context)

def facultDetailView(request,url):
    pageCats = PageCategory.objects.all()
    facult = Facult.objects.get(slug=url)
    departments = Department.objects.filter(facult=facult)
    internatiolization = PageCategory.objects.get(id=3)
    context = {
        'facult':facult,
        'departments':departments,
        'pageCats':pageCats,
        'internatiolization':internatiolization
    }

    return render(request,'facult/facultDetail.html',context)

    
