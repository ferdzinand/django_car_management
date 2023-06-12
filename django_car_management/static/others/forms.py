from django import forms
from .models import Car

class CarForm(forms.ModelForm):
   class Meta:
       model = Car
       fields = ('origin','brand','model', 'year', 'color')
       labels = {
          'brand':'Brand',
           'model': 'Model',
           'year': 'Year',
           'color': 'Color',
        }
