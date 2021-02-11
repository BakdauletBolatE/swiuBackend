from modeltranslation.translator import register,TranslationOptions
from .models import Post,Quote


@register(Quote)
class FacultTranslationOptions(TranslationOptions):

    fields = ('title','description','author')

@register(Post)
class FacultTranslationOptions(TranslationOptions):

    fields = ('title','description')