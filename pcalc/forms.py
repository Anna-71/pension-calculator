from django.utils.translation import ugettext_lazy as _
from .models import Pcalc_info
from django.forms import ModelForm,  TextInput, Select
from django import forms


class Pcalc_infoForm(forms.ModelForm):
    class Meta:
        model = Pcalc_info
        fields = (
            'sex', 'year_born','year_begin',
            'ts01', 'ts91', 'szar5', 'szar2',
            'ts14','szar14',
            'szar15', 'sam', 'ssam', 'army', 'child', 'other',
            'stn1', 'stn2', 'sts',  'stl1', 'stl2')

     #   labels = {'year_born': "Ваш год рождения:", 'year_begin': "Год начала Вашей трудовой деятельности:" }

          
        widgets = {
            'sex' : forms.Select(attrs={'class':'custom-select d-block w-100 form-control'}),
            'year_born':forms.TextInput(attrs={'class' : 'form-control'}),
            'year_begin':forms.TextInput(attrs={'class' : 'form-control'}),
            'ts01' : forms.TextInput(attrs={'class' : 'form-control'}),
            'ts91' : forms.TextInput(attrs={'class' : 'form-control'}),
            'szar5': forms.TextInput(attrs={'class' : 'form-control'}),
            'szar2': forms.TextInput(attrs={'class' : 'form-control'}),
            'ts14' : forms.TextInput(attrs={'class' : 'form-control'}),
            'szar14': forms.TextInput(attrs={'class' : 'form-control'}),
            'szar15': forms.TextInput(attrs={'class' : 'form-control'}),
            'sam': forms.TextInput(attrs={'class' : 'form-control'}),
            'ssam': forms.TextInput(attrs={'class' : 'form-control'}),
            'army': forms.TextInput(attrs={'class' : 'form-control'}),
            'child': forms.TextInput(attrs={'class' : 'form-control'}),
            'other': forms.TextInput(attrs={'class' : 'form-control'}),
            'stn1': forms.TextInput(attrs={'class' : 'form-control'}),
            'stn2': forms.TextInput(attrs={'class' : 'form-control'}),
            'sts': forms.TextInput(attrs={'class' : 'form-control'}),
            'stl1': forms.TextInput(attrs={'class' : 'form-control'}),
            'stl2': forms.TextInput(attrs={'class' : 'form-control'}),
            }
