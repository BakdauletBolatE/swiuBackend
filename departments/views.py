from django.shortcuts import render
from .models import Department,ActivityDepartment,EducationalPrograms
from staff.models import Staff
from faculties.models import PageCategory


def departmentDetailView(request,url):

    department = Department.objects.get(slug=url)

    activityDepartments = ActivityDepartment.objects.filter(department=department)
    eduPros = EducationalPrograms.objects.filter(department=department)

    staffEdus = Staff.objects.filter(department=department)

    pageCats = PageCategory.objects.all()


    context = {
        'department':department,
        'activityDepartments':activityDepartments,
        'eduPros':eduPros,
        'staffEdus':staffEdus,
        'pageCats':pageCats,
    }

    return render(request,'departments/departmentDetail.html',context)

def eduProgramDetail(request, url):
    pageCats = PageCategory.objects.all()
    
    eduProgram = EducationalPrograms.objects.get(slug=url)

    eduStuffs = Staff.objects.filter(educationalPrograms=eduProgram)

    context = {
        'eduStuffs':eduStuffs,
        'eduProgram':eduProgram,
        'pageCats':pageCats,
    }

    return render(request,'departments/eduprogramDetail.html',context)


