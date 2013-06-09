from django import forms
from django.forms.models import ModelForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import os.path
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm): 
    # add placeholder attributes
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email'}))
    password1 = forms.CharField(label=("Password"),widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(label=("Password confirmation"),widget=forms.PasswordInput(attrs={'placeholder':'Password'}),help_text = ("Enter the same password as above, for verification."))
    class Meta:
        model = User
        fields = ('username', 'email',) 
    def clean_email(self):
        """
        Validate that the supplied email address is unique for the
        site.
        
        """
        email = self.cleaned_data["email"]
        try:
            User.objects.get(email__iexact=email)
        except User.DoesNotExist:
            return self.cleaned_data["email"]
        raise forms.ValidationError((u'This email is already in use. Please choose another.'))
    def save(self, profile_callback=None,commit=True,fail_silently=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email"]
        user.is_active = True # change to false if using email activation
        if commit:
            user.save()
        return user


class PostForm(forms.Form): 
    rawdata = forms.CharField(label='Raw data')
