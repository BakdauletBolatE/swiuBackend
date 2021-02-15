from django.contrib import admin
from modeltranslation.admin import TranslationAdmin


from .models import *

# Register your models here.


@admin.register(Facult)
class FacultAdmin(TranslationAdmin):
    
    prepopulated_fields = {"slug": ("name",)}

class PagePhotoTabulerInline(admin.TabularInline):
    model = PageImages

@admin.register(Page)
class PageAdmin(TranslationAdmin):
    prepopulated_fields = {"slug": ("title",)}
    inlines = [PagePhotoTabulerInline]

@admin.register(PageCategory)
class PageCatAdmin(TranslationAdmin):

    list_display = ('name',)



admin.site.register(PageImages)