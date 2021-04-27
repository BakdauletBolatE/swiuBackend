from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import *

# Register your models here.
class YearAdmin(TranslationAdmin):
    prepopulated_fields = {"slug": ("year",)}

admin.site.register(Year,YearAdmin)

class BookAdmin(TranslationAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Book,BookAdmin)


admin.site.register(RegistrationCategory)
admin.site.register(Registration)