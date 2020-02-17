from django import forms
from front.models import User


class RegisterForm(forms.ModelForm):

    password_repeat = forms.CharField(max_length=20)

    def clean(self):
        clean_data = super(RegisterForm, self).clean()
        password = clean_data.get('password')
        password_repeat = clean_data.get('password_repeat')
        if password != password_repeat:
            raise forms.ValidationError('两次密码输入不一致')
        return clean_data

    class Meta:

        model = User
        fields = ['username', 'password', 'email']


class LoginForm(forms.ModelForm):

    class Meta:

        model = User
        fields = ['email', 'password']


class TransForm(forms.Form):

    email = forms.CharField(max_length=100)
    money = forms.FloatField()
