from django import forms
from .models import Lop, Student

# form add class


class list_class_form(forms.ModelForm):
    class Meta:
        model = Lop
        fields = ['name_class', 'descriptions']

# form add student in class

class addStudent(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'id_student', 'detail_per']
