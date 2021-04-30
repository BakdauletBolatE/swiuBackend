from modeltranslation.translator import register,TranslationOptions
from .models import WidgetOnlyText, WidgetPhoto,WidgetText


@register(WidgetOnlyText)
class FacultTranslationOptions(TranslationOptions):

    fields = ('description',)

@register(WidgetPhoto)
class FacultTranslationOptions(TranslationOptions):

    fields = ('title','description')


@register(WidgetText)
class SlideTranslationOptions(TranslationOptions):

    fields = ('title','description')