from django.shortcuts import render
from departments.models import EducationalPrograms

# Create your views here.

def index(request):
    eduPros = EducationalPrograms.objects.all()
    context = {
        'eduPros':eduPros
    }
    return render(request,'swiupanel/index.html',context)