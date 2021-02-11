from django.shortcuts import render
from .models import Facult
from departments.models import Department
from .models import PageCategory

# Create your views here.

def facultView(request):

    facults = Facult.objects.all()
    pageCats = PageCategory.objects.all()
    context = {
        'facults':facults,
        'pageCats':pageCats
    }
    return render(request,'facult/index.html',context)

def facultDetailView(request,url):
    pageCats = PageCategory.objects.all()
    facult = Facult.objects.get(slug=url)
    departments = Department.objects.filter(facult=facult)
    context = {
        'facult':facult,
        'departments':departments,
        'pageCats':pageCats
    }

    return render(request,'facult/facultDetail.html',context)

    
