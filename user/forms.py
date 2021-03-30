from django import forms
from pyfull.validators import PhoneValidator
from django.core.validators import MaxLengthValidator
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ValidationError
from .models import User

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(max_length=50, widget=forms.PasswordInput, required=True,
                              validators=[MaxLengthValidator(6)])

    confirm = forms.CharField(max_length=50, widget=forms.PasswordInput, required=True,
                              validators=[MaxLengthValidator(6, message='Salom')])



    class Meta:
        model = User
        fields = ('username', 'phone', 'password', 'confirm')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)


class EditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'phone', 'first_name', 'last_name', 'email']


    # username = forms.CharField(max_length=20, required=True,
    #                            validators=[UnicodeUsernameValidator()])
    # phone = forms.CharField(max_length=15, required=True,
    #                         validators=[PhoneValidator()])
    # password = forms.CharField(max_length=50, widget=forms.PasswordInput, required=True,
    #                            validators=[MaxLengthValidator(6)])
    # confirm = forms.CharField(max_length=50, widget=forms.PasswordInput, required=True,
    #                           validators=[MaxLengthValidator(6)])
    #
    # def clean_username(self):
    #     if User.objects.filter(username=self.cleaned_data.get("username")).exists():
    #         raise ValidationError('Ushbu nickname band')
    #     return self.cleaned_data['username']
    #
    # def clean_phone(self):
    #     if User.objects.filter(phone=self.cleaned_data.get("phone")).exists():
    #         raise ValidationError('Ushbu telfon raqam band')
    #     return self.cleaned_data['phone']
    #
    # def clean_confirm(self):
    #     if self.cleaned_data['password'] != self.cleaned_data['confirm']:
    #         raise ValidationError('Parollar bir xil emas iltimos tekshiring')
    #     return self.cleaned_data['confirm']
