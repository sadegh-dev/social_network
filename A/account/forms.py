from django import forms

messages1 = {
    'required':'این فیلد اجباری است',
    'invalid':'لطفا یک ایمیل معتبر وارد کنید',
    'max_length':'لطفا حداکثر طول ورودی را رعایت کنید'
}

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter username'}))
    password = forms.CharField(max_length=40, widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter password'}))


class UserRegistrationForm(forms.Form):
    username = forms.CharField(error_messages=messages1, max_length=30, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter username'}))
    email = forms.EmailField(error_messages=messages1, max_length=50, widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'}))
    password = forms.CharField(error_messages=messages1, max_length=40, widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter password'}))



