from modeltranslation.translator import register,TranslationOptions
from .models import Post,Quote,Slides


@register(Quote)
class FacultTranslationOptions(TranslationOptions):

    fields = ('title','description','author')

@register(Post)
class FacultTranslationOptions(TranslationOptions):

    fields = ('title', 'description', 'short_description')


@register(Slides)
class SlideTranslationOptions(TranslationOptions):

    fields = ('subTitle','title','btn','btn2')