from django import forms

class login(forms.Form):
    Username = forms.CharField(max_length=100)
    Password = forms.CharField(max_length=100)


class signup(forms.Form):
    Username = forms.CharField(max_length=100)
    First_Name = forms.CharField(max_length=100)
    Last_Name = forms.CharField(max_length=100)
    Address = forms.CharField(max_length=100)
    Email = forms.EmailField(max_length=100)
    Password = forms.CharField(max_length=100,widget=forms.PasswordInput)
    Confirm_Password = forms.CharField(max_length=100,widget=forms.PasswordInput)

class amount(forms.Form):
    Amount = forms.IntegerField()