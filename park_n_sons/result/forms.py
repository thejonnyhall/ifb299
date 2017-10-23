from django import forms

OPTIONS = (
    ('asc', 'Name Ascending'),
    ('desc', 'Name Descending'),
    ('rate', 'Rating'),
)

class SortForm(forms.Form):
    sort = forms.ChoiceField(label='Sort By', choices=OPTIONS, required=False)