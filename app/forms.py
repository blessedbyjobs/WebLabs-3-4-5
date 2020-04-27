from django import forms

from .models import *


class SubjectForm(forms.ModelForm):

    name = forms.CharField(required=True)
    hour = forms.IntegerField(required=True)

    class Meta:
        model = Subject
        fields = ('name', 'hour')
