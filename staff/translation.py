from modeltranslation.translator import register,TranslationOptions
from .models import Position,StaffCat,Staff


@register(Position)
class FacultTranslationOptions(TranslationOptions):

    fields = ('name',)

@register(StaffCat)
class FacultTranslationOptions(TranslationOptions):

    fields = ('name',)

@register(Staff)
class FacultTranslationOptions(TranslationOptions):

    fields = ('name','about')