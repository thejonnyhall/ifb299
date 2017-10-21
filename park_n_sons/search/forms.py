from django import forms

USERTYPE = (
    ('bsns','Businessman'),
    ('trst','Tourist'),
    ('sdnt','Student'),
)

class SearchForm(forms.Form):
    keywords = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Search'}), required=False)
    userType = forms.ChoiceField(label='', choices=USERTYPE)
    free = forms.BooleanField(label='Free Activity', required=False)
    publicTransport = forms.BooleanField(label='Accessible by Public Transport', required=False)
    childFriendly = forms.BooleanField(label='Child Friendly', required=False)