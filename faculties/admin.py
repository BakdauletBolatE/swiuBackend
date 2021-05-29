from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from django_summernote.admin import SummernoteModelAdmin

from .models import *

# Register your models here.


@admin.register(Facult)
class FacultAdmin(TranslationAdmin):
    
    prepopulated_fields = {"slug": ("name",)}

class PagePhotoTabulerInline(admin.TabularInline):
    model = PageImages

@admin.register(Page)
class PageAdmin(SummernoteModelAdmin,TranslationAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title','order','category')
    list_filter = ('category',)
    summernote_fields = ('content_ru', 'content_en', 'content_kk')
    ordering = ['order']
    search_fields = ['title']
    inlines = [PagePhotoTabulerInline]

@admin.register(PageCategory)
class PageCatAdmin(TranslationAdmin):

    list_display = ('name',)



admin.site.register(PageImages)
