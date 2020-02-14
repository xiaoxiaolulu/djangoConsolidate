from django import forms
from front.models import User


class RegisterForm(forms.ModelForm):

    password_repeat = forms.CharField(max_length=16, min_length=6)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        password_repeat = cleaned_data.get('password_repeat')
        if password != password_repeat:
            raise forms.ValidationError(message="两次密码输入不一致")
        return cleaned_data

    class Meta:
        model = User
        fields = '__all__'


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']
