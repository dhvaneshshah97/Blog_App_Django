from django import forms
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm

## why we create this form? so the answer is -> indeed, django provides the default UserCreationForm, but we wanted to add an email field, so that's why.
class UserRegisterForm(UserCreationForm):   ## inherits UserCreationForm
    email = forms.EmailField()  

    class Meta:     ## gives us nested namespace for configurations
        model = User
        fields = ['username', 'email' , 'password1', 'password2']       ## this fields are shown in this order in form