from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['origin','brand', 'model', 'year', 'color']
        labels = {
            'origin':'Origin',
            'brand': 'Brand',
            'model': 'Model',
            'year': 'Year',
            'color': 'Color'

        }
        widgets = {
            'year': forms.NumberInput(attrs={'min': 1900, 'max': 2100}),
        }