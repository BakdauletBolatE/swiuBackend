from django.contrib import admin
from .models import *
from django import forms
from django.utils.functional import lazy



# Register your models here.


class DepartmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Department,DepartmentAdmin)

class EducationalProgramsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(EducationalPrograms,EducationalProgramsAdmin)
admin.site.register(EducationalProgramsCat)


class ActivityDetailsInline(admin.TabularInline):
    model = ActivityDepartmentFoto

class ActivityChoiceField(forms.ModelChoiceField):
    pass

class ActivityAdmin(admin.ModelAdmin):

    inlines = [ActivityDetailsInline]
    prepopulated_fields = {"slug": ("title",)}
    
admin.site.register(ActivityDepartment, ActivityAdmin)
admin.site.register(ActivityDepartmentFoto)

class ActivityDepartmentCatAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(ActivityDepartmentCat,ActivityDepartmentCatAdmin)


