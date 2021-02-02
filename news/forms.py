from django import forms

from .models import Questions

class QuestionsForm(forms.ModelForm):
    title = forms.CharField(label='Заголовок вашего вопроса', 
                            max_length=100,
                            widget=forms.TextInput(attrs={'class': 'review__form'}))
    description = forms.Field (label='Описание вашего вопроса', 
                            
                            widget=forms.Textarea(attrs={'class': 'review__form'}))

    class Meta:
        model = Questions
        fields = ('title', 'description',)                   

