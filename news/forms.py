from django import forms

from .models import Questions,PostComments

class QuestionsForm(forms.ModelForm):
    title = forms.CharField(label='Заголовок вашего вопроса', 
                            max_length=100,
                            widget=forms.TextInput(attrs={'class': 'review__form'}))
    description = forms.Field (label='Описание вашего вопроса', 
                            
                            widget=forms.Textarea(attrs={'class': 'review__form'}))

    class Meta:
        model = Questions
        fields = ('title', 'description',) 

                  
class PostCommentsForm(forms.ModelForm):

    title = forms.CharField(label='Укажите закгаловок коментарий',
                            max_length=100,
                            widget=forms.TextInput(attrs={
                                'class':'review__form'
                            }))

    description = forms.Field(label='Описание вашего вопроса',  
                            widget=forms.Textarea(attrs={
                                'class': 'review__form'
                            }))

    class Meta:
        model = PostComments
        fields = ('title', 'description',) 