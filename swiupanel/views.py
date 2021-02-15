from django.http.request import HttpHeaders
from faculties.models import Facult
from django import forms
from django.shortcuts import render,redirect
from departments.models import EducationalPrograms,Department
from faculties.models import Page
from .forms import EduForm,StuffForm
from staff.models import Staff
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import permission_required



# Create your views here.

@permission_required('departments.add_educationalprograms')
def index(request):
    eduPros = EducationalPrograms.objects.all()
    staffs = Staff.objects.all()
    context = {
        'eduPros':eduPros,
        'staffs':staffs
    }
    return render(request,'swiupanel/index.html',context)

def staffListView(request):
    staffs = Staff.objects.all()
    context = {
        'staffs':staffs
    }
    return render(request,'swiupanel/Staff/listView.html',context)

def eduProListView(request):
    eduPros = EducationalPrograms.objects.all()
    context = {
        'eduPros':eduPros,
    }
    return render(request,'swiupanel/EducationalPrograms/listView.html',context)

def addEdu(request):
    
    if request.method == "POST":
        form = EduForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('swiuindex')
    else:
        form = EduForm()
        context = {
        'form':form
        }
        return render(request,'swiupanel/EducationalPrograms/add.html',context)
    

def getDepartments(request,*args,**kwargs):
    facult = kwargs.get('fac')
    departments = list(Department.objects.filter(facult_id=facult).values())

    return JsonResponse({'data':departments})



def addStaff(request):
    if request.method == "POST":
        form = StuffForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('swiuindex')

    else:
        form = StuffForm()
        context = {
        'form':form
        }
        return render(request,'swiupanel/Staff/add.html',context)

def editStaff(request,url):
    if request.method == "POST":
        form = StuffForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('swiuindex')
       
       
            
    else:
        staff = Staff.objects.get(slug=url)
        form = StuffForm(request.POST or None,request.FILES or None,instance=staff)
        context = {
        'form':form,
        'id':staff.staffCat.id
        }
        return render(request,'swiupanel/Staff/edit.html',context)

def getFacultStaff(request,*args,**kwargs):
    staffCat = kwargs.get('cat')
    if staffCat == "1":
        data = list(Page.objects.values())
    else:
        data = list(Facult.objects.values())

    return JsonResponse({'data':data})

def getOpJson(request,*args,**kwargs):
    op = kwargs.get('op')
    data = list(EducationalPrograms.objects.filter(department_id=op).values())

    return JsonResponse({'data':data})