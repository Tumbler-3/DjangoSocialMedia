from django.forms import ModelForm
from User.models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class CustomUserLoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = AuthenticationForm.field_order
     
class CustomUserRegistrtionForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('name',) + UserCreationForm.Meta.fields + ('email',)