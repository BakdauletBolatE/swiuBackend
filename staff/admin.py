from django.contrib import admin
from .models import *
# Register your models here.

class PositionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Position,PositionAdmin)

class StaffCatAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('id', 'name')
    
admin.site.register(StaffCat,StaffCatAdmin)

class StaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','staffCat')
    prepopulated_fields = {"slug": ("name",)}
    
admin.site.register(Staff,StaffAdmin)