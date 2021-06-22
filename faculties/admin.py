from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from django_summernote.admin import SummernoteModelAdmin
from adminsortable2.admin import SortableAdminMixin

from .models import *

# Register your models here.


@admin.register(Facult)
class FacultAdmin(TranslationAdmin):
    
    prepopulated_fields = {"slug": ("name",)}

class PagePhotoTabulerInline(admin.TabularInline):
    model = PageImages

@admin.register(Page)
class PageAdmin(SortableAdminMixin, SummernoteModelAdmin,TranslationAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title','order','category')
    list_filter = ('category','order')
    summernote_fields = ('content_ru', 'content_en', 'content_kk')
    search_fields = ['title']
    inlines = [PagePhotoTabulerInline]

@admin.register(PageCategory)
class PageCatAdmin(SortableAdminMixin, TranslationAdmin):

    list_display = ('name', 'order')



admin.site.register(PageImages)
