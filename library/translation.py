from modeltranslation.translator import register,TranslationOptions
from .models import Book,Year


@register(Book)
class FacultTranslationOptions(TranslationOptions):

    fields = ('name','description')

@register(Year)
class FacultTranslationOptions(TranslationOptions):

    fields = ('year',)