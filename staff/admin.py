from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *
# Register your models here.

class PositionAdmin(TranslationAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Position,PositionAdmin)

class StaffCatAdmin(TranslationAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('id', 'name')
    
admin.site.register(StaffCat,StaffCatAdmin)

class StaffAdmin(TranslationAdmin):
    list_display = ('id', 'name','staffCat')
    prepopulated_fields = {"slug": ("name",)}
    
admin.site.register(Staff,StaffAdmin)

admin.site.register(Profile)