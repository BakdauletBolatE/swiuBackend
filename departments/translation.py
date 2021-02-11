from modeltranslation.translator import register,TranslationOptions
from .models import Department,EducationalProgramsCat,EducationalPrograms,ActivityDepartmentCat,ActivityDepartment


@register(Department)
class FacultTranslationOptions(TranslationOptions):

    fields = ('name','description')

@register(EducationalProgramsCat)
class FacultTranslationOptions(TranslationOptions):

    fields = ('name',)

@register(EducationalPrograms)
class FacultTranslationOptions(TranslationOptions):

    fields = ('name','description')

@register(ActivityDepartmentCat)
class FacultTranslationOptions(TranslationOptions):

    fields = ('name',)

@register(ActivityDepartment)
class FacultTranslationOptions(TranslationOptions):

    fields = ('title','short_description','description')


