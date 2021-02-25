from django.http.request import HttpHeaders
from faculties.models import Facult
from django.shortcuts import render,redirect
from departments.models import ActivityDepartmentFoto, EducationalPrograms,Department,ActivityDepartment
from faculties.models import Page
from .forms import EduForm,StuffForm,ActivityDepForm,ActivityDepCatForm
from staff.models import Staff
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import permission_required
from django.contrib import messages



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

#@permission_required()
def staffListView(request):
    staffs = Staff.objects.all()
    context = {
        'staffs':staffs
    }
    return render(request,'swiupanel/Staff/listView.html',context)

#@permission_required()
def eduProListView(request):
    eduPros = EducationalPrograms.objects.all()
    context = {
        'eduPros':eduPros,
    }
    return render(request,'swiupanel/EducationalPrograms/listView.html',context)

#@permission_required()
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
    
#@permission_required()
def getDepartments(request,*args,**kwargs):
    facult = kwargs.get('fac')
    departments = list(Department.objects.filter(facult_id=facult).values())

    return JsonResponse({'data':departments})


#@permission_required()
def addStaff(request):
    if request.method == "POST":
        form = StuffForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,str(request.POST.get('name_ru'))+'Новость добавлен успешно')
            return redirect('addStaff')
        else:
            messages.error(request,str(request.POST.get('name_ru'))+'Ошибка при добавлений')
            return redirect('addStaff')

    else:
        form = StuffForm()
        context = {
        'form':form
        }
        return render(request,'swiupanel/Staff/add.html',context)

#@permission_required()
def editStaff(request,url):
    if request.method == "POST":
        staff = Staff.objects.get(slug=url)
        form = StuffForm(request.POST or None, request.FILES or None,instance=staff)
        if form.is_valid():
            form.save()
            return redirect('staffListView')
        else:
            return HttpResponse(form)

    else:
        staff = Staff.objects.get(slug=url)
        form = StuffForm(request.POST or None,request.FILES or None,instance=staff)
        context = {
        'form':form,
        'id':staff.staffCat.id,
        'url': url
        }
        return render(request,'swiupanel/Staff/edit.html',context)

#@permission_required()
def getFacultStaff(request,*args,**kwargs):
    staffCat = kwargs.get('cat')
    if staffCat == "1":
        data = list(Page.objects.values())
    elif staffCat == "2":
        data = list(Page.objects.values())
    else:
        data = list(Facult.objects.values())

    return JsonResponse({'data':data})

# @permission_required()
def getOpJson(request,*args,**kwargs):
    op = kwargs.get('op')
    data = list(EducationalPrograms.objects.filter(department_id=op).values())

    return JsonResponse({'data':data})

# @permission_required()
def searchEdu(request,*args,**kwargs):

    qs = kwargs.get('search');

    s_data = list(EducationalPrograms.objects.values())
    d_data = []
    for i in range(1,len(s_data)):
        if qs in s_data[i]['name']:
            d_data.append(s_data[i])
        
    data = d_data

    return JsonResponse({'data':data})

def activDepAdd(request):

    if request.method == "POST":
        form = ActivityDepForm(request.POST or None,request.FILES or None)
        if form.is_valid():

            images = request.FILES.getlist('images')
            t = form.save()

            if images:
                dep = ActivityDepartment.objects.get(id=t.id)
                for img in images:
                    d = ActivityDepartmentFoto.objects.create(
                        photo=img,
                        department=dep 
                    )
                    d.save()

            messages.success(request,str(request.POST.get('title'))+'Новость добавлен успешно')
            return redirect('activDepAdd')
        else:
            messages.error(request,str(request.POST.get('title'))+'Ошибка при добавлений')
            return redirect('activDepAdd')

    else:
        form = ActivityDepForm()
        context = {
        'form':form
        }
        return render(request,'swiupanel/Activity/add.html',context)

def activDepList(request):

    activityDeps = ActivityDepartment.objects.all()
    
    context = {
        'activityDeps':activityDeps
    }
    return render(request,'swiupanel/Activity/index.html',context)


def activDepCatAdd(request):

    if request.method == "POST":
        form = ActivityDepCatForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('staffListView')

    else:
        form = ActivityDepCatForm()
        context = {
        'form':form
        }
        return render(request,'swiupanel/ActivityCat/add.html',context)