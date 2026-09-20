from django import forms
from .models import Restaurant


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'specialization', 'address', 'website', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'specialization': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }


class RestaurantSearchForm(forms.Form):
    specialization = forms.CharField(required=False, label='',
                                      widget=forms.TextInput(attrs={
                                          'class': 'form-control',
                                          'placeholder': 'Search by specialization'
                                      }))
