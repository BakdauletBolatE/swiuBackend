
from django import forms
from departments.models import EducationalPrograms,ActivityDepartment,ActivityDepartmentCat
from staff.models import Staff
from faculties.models import Page
from .models import WidgetItems


class EduForm(forms.ModelForm):

    name = forms.CharField(label='Заголовок вашего вопроса', 
                            max_length=100,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.Field (label='Описание вашего вопроса', 
                            
                            widget=forms.Textarea(attrs={'class': 'form-control'}))

    

    class Meta:
        model = EducationalPrograms
        fields = ('name', 'description','facult','department','img','slug','cat') 



class StuffForm(forms.ModelForm):
    name_ru = forms.CharField(label='Имя сотрудника(руский)', 
                            max_length=100,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    slug = forms.CharField(label='url сотрудника', 
                            max_length=100,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    name_en = forms.CharField(label='Staff name(engilsh)', 
                            max_length=100,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    name_kk = forms.CharField(label='Жұмысшының есімі(қазақша)', 
                            max_length=100,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    email = forms.EmailField(label='Email сотрудника', 
                            widget=forms.EmailInput(attrs={'class': 'form-control'}))
    
    adress = forms.CharField(label='Адрес сотрудника', 
                            max_length=100,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    phone = forms.CharField(label='Телефон сотрудника', 
                            max_length=100,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))

    about_ru = forms.Field(label='Краткое описание сотрдуника', 
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    about_en = forms.Field(label='Short description about staff', 
                            widget=forms.TextInput(attrs={'class': 'form-control'}))

    about_kk = forms.Field(label='Жұмыскер бойынша қысқаша ақпарат', 
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Staff
        fields = ('name_ru','name_en','name_kk','img','email','adress','slug','phone','about_ru','about_en','about_kk','staffCat','facult','department','educationalPrograms','page') 

class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ('title','url','slug','category')


class WidgetItemsForm(forms.ModelForm):

    class Meta:

        model = WidgetItems
        fields = ('__all__')

class ActivityDepForm(forms.ModelForm):

   
    
    slug = forms.CharField(label='url деятельности кафедры', 
                            max_length=100,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    short_description = forms.Field(label='Описание деятельности кафедры(ru)', 
                           
                            widget=forms.Textarea(attrs={'class': 'form-control'}))

    short_description_en = forms.Field(label='Описание деятельности кафедры(en)', 
                           
                            widget=forms.Textarea(attrs={'class': 'form-control'}))

    short_description_kk = forms.Field(label='Описание деятельности кафедры(kk)', 
                           
                            widget=forms.Textarea(attrs={'class': 'form-control'}))

    description = forms.Field(label='Полное описание деятельности кафедры', 
                            
                            widget=forms.Textarea(attrs={'class': 'form-control'}))
    
    
    class Meta:

        model = ActivityDepartment
        fields = ('__all__')


class ActivityDepCatForm(forms.ModelForm):

    class Meta:

        model = ActivityDepartmentCat
        fields = ('__all__')