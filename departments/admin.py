from django.contrib import admin
from .models import *
from django import forms
from modeltranslation.admin import TranslationAdmin



# Register your models here.


class DepartmentAdmin(TranslationAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Department,DepartmentAdmin)

class EducationalProgramsAdmin(TranslationAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(EducationalPrograms,EducationalProgramsAdmin)
admin.site.register(EducationalProgramsCat)


class ActivityDetailsInline(admin.TabularInline):
    model = ActivityDepartmentFoto


class ActivityAdmin(TranslationAdmin):

    inlines = [ActivityDetailsInline]
    prepopulated_fields = {"slug": ("title",)}
    
admin.site.register(ActivityDepartment, ActivityAdmin)
admin.site.register(ActivityDepartmentFoto)

class ActivityDepartmentCatAdmin(TranslationAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(ActivityDepartmentCat,ActivityDepartmentCatAdmin)


