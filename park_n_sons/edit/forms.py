from django import forms

class AddForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    address = forms.CharField(label='Address', max_length=100)
    suburb = forms.CharField(label='Suburb', max_length=100)
    latitude = forms.FloatField(label='Latitude')
    longitude = forms.FloatField(label='Longitude')

class ModifyForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    address = forms.CharField(label='Address', max_length=100)
    suburb = forms.CharField(label='Suburb', max_length=100)
    latitude = forms.FloatField(label='Latitude')
    longitude = forms.FloatField(label='Longitude')