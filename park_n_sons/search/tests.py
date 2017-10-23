from django.test import TestCase
from search.forms import SearchForm
# Create your tests here.

class searchtests(TestCase):
    def test_form(self):
        form_data = {'userType':'Businessman'}
        form = SearchForm(data=form_data)
        self.assertTrue(form.is_valid())
