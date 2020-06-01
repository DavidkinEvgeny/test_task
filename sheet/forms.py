from django import forms
from .models import Sheet


class SheetForm(forms.ModelForm):
    '''Форма записи'''
    class Meta:
        model = Sheet
        fields = ['title', 'content', 'date_event']
        widgets = {
            'title': forms.TextInput(),
            'content': forms.Textarea(),
            'date_event': forms.DateTimeInput(),
        }