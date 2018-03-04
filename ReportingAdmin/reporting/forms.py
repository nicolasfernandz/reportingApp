from django import forms
from django.contrib.auth.models import User

class GetReportingForm(forms.Form):
    #cada atributo corresponde con el atributo name en el html
    observaciones = forms.CharField(label='ovserbaciones', max_length=250)
    
class RegistrationForm(forms.Form):
    first_name = forms.CharField(label="username", max_length=150, required=True)
    last_name = forms.CharField(label="userSurName", max_length=150, required=True)
    email = forms.EmailField(label="email", max_length=200)
    password = forms.PasswordInput()
    repitPassword = forms.PasswordInput()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', )