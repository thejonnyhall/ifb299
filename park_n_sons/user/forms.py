from django import forms
import re
from django.contrib.auth.models import User, Group
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import UserCreationForm

USERTYPE = (
    ('bsns','Businessman'),
    ('trst','Tourist'),
    ('sdnt','Student'),
)

class UserCreateForm(UserCreationForm):
    UserType = forms.ChoiceField(label='', choices=USERTYPE)

    class Meta:
        model = User
        fields = ("username", "UserType","password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        if commit:
            user.save()
        return user
