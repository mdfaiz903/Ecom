from django import forms 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation

#Registration 

class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class':'form-control'})
        )
    password2 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class':'form-control'})
        )
    email = forms.CharField(
        label='Email',
        required=True,
        widget=forms.EmailInput(attrs={'class':'form-control'})
    )
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}




class LoginForm(AuthenticationForm):
    username =UsernameField(
        widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'})

    )
    password = forms.CharField(
        label=_('Password'),strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete':'current_password','class':'form-control'})
    )



#passwoed change
class Mypasswoedchangeform(PasswordChangeForm):
    old_password = forms.CharField(label=_('Old Password'),
                                   strip=False,
                                   widget=forms.PasswordInput(
                                       attrs={'autocomplete':'current-password',
                                              'autofocus':True,
                                              'class':'form-control'}
                                   ),
                                   help_text=password_validation.password_validators_help_text_html()
                                   )
    new_password1 = forms.CharField(label=_('New Password'),strip=False,
                                   widget=forms.PasswordInput(
                                       attrs={'autocomplete':'current-password','autofocus':True,'class':'form-control'}
                                   ))
    new_password2 = forms.CharField(label=_('Confirm Password'),strip=False,
                                   widget=forms.PasswordInput(
                                       attrs={'autocomplete':'current-password','autofocus':True,'class':'form-control'}
                                   ))


class MypasswordResetform(PasswordResetForm):
    email = forms.EmailField(label=_('Email'),
                             max_length=255,
                             widget=forms.EmailInput(
                                 attrs={'autocomplete':'email','autofocus':True,'class':'form-control'}
                                                                    )
                             )
    



#set password foem

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_('New Password'),strip=False,
                                   widget=forms.PasswordInput(
                                       attrs={'autocomplete':'current-password','autofocus':True,'class':'form-control'}
                                   ))
    new_password2 = forms.CharField(label=_('Confirm Password'),strip=False,
                                   widget=forms.PasswordInput(
                                       attrs={'autocomplete':'current-password','autofocus':True,'class':'form-control'}
                                    ))