
from modeltranslation.translator import register,TranslationOptions
from .models import Facult,Page, PageCategory


@register(Facult)
class FacultTranslationOptions(TranslationOptions):

    fields = ('name','description')

@register(Page)
class PageTranslationOptions(TranslationOptions):

    fields = ('content','title')

@register(PageCategory)
class PageCatTranslationOptions(TranslationOptions):

    fields = ('name',)