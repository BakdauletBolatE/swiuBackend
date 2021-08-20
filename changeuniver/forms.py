from django import forms
from .models import Zayavka, Shifr
from departments.models import EducationalPrograms
from django.conf import settings

class ZayavkaApp(forms.ModelForm):
    rejim = (
        ('Қашықтан', 'Қашықтан'),
        ('Күндізгі', 'Күндізгі')
    )

    lang = (
        ('Қазақ', 'Қазақ'),
        ('Орыс', 'Орыс')
    )
    shifr_name = forms.ModelChoiceField(queryset=EducationalPrograms.objects.all(), to_field_name="id",widget=forms.Select(attrs={'class': 'form-select'}) )
    language = forms.ChoiceField(choices=lang, widget=forms.Select(attrs={'class': 'form-select'}))
    rejim = forms.ChoiceField(choices=rejim, widget=forms.Select(attrs={'class': 'form-select'}))
    
    class Meta:
        model = Zayavka
        fields = ['surname','name','last_name', 'shifr_name', 'course', 'top', 'phone', 'rejim', 'language',]

        widgets = {
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', }),
            'last_name': forms.TextInput(attrs={'class': 'form-control', }),
            
            'course': forms.TextInput(attrs={'class': 'form-control'}),
            'top': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            }