from django import forms
from .models import Lop


class list_class_form(forms.ModelForm):
    class Meta:
        model = Lop
        fields = ['name_class', 'descriptions']
