from django.shortcuts import render
from .models import Department,ActivityDepartment,EducationalPrograms
from staff.models import Staff
from faculties.models import PageCategory
from django.core.paginator import Paginator


def departmentDetailView(request,url):

    department = Department.objects.get(slug=url)
    activityDepartments = ActivityDepartment.objects.filter(department=department)
    paginator = Paginator(activityDepartments, 5) # Show 5 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    eduPros = EducationalPrograms.objects.filter(department=department)
    staffEdus = Staff.objects.filter(department=department)

    context = {
        'department':department,
        'activityDepartments':page_obj,
        'eduPros':eduPros,
        'staffEdus':staffEdus,        
    }

    return render(request,'departments/departmentDetail.html',context)

def eduProgramDetail(request, url):

    eduProgram = EducationalPrograms.objects.get(slug=url)
    eduStuffs = Staff.objects.filter(educationalPrograms=eduProgram)
    context = {
        'eduStuffs':eduStuffs,
        'eduProgram':eduProgram,
    }

    return render(request,'departments/eduprogramDetail.html',context)


