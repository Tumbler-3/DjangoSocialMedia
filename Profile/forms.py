from django import forms
from User.models import CustomUser
from phonenumber_field.formfields import PhoneNumberField

class ProfileChangeForm(forms.ModelForm):
    username = forms.CharField(required=False)
    class Meta:
        model = CustomUser
        fields = ['name','username','email', 'phone']
        