from django import forms

class SearchForm(forms.Form):
    keywords = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Search'}), required=False)
    free = forms.BooleanField(label='Free Activity', required=False)
    publicTransport = forms.BooleanField(label='Accessible by Public Transport', required=False)
    childFriendly = forms.BooleanField(label='Child Friendly', required=False)