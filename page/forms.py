from django import forms
from .models import WidgetText,WidgetPhoto,WidgetOnlyText

class WidgetTextForm(forms.ModelForm):

    class Meta:
        model = WidgetText
        fields = ('__all__')

class WidgetOnlyTextForm(forms.ModelForm):

    class Meta:
        model = WidgetOnlyText
        fields = ('__all__')

class WidgetPhotoForm(forms.ModelForm):

    class Meta:
        model = WidgetPhoto
        fields = ('__all__')

