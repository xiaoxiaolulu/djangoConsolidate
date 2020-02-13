from django import forms
from django.core import validators

from front.models import User


class MessageBoardForm(forms.Form):
    title = forms.CharField(max_length=100, min_length=2, label="标题")
    content = forms.CharField(widget=forms.Textarea, label='内容')
    email = forms.EmailField(validators=[validators.EmailValidator('请输入正确格式的邮箱')], label='邮箱')
    replay = forms.BooleanField(required=False, label='回复')


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    telephone = forms.CharField(validators=[validators.RegexValidator(r'1[345678]\d{9}', message='请输入正确的手机号码')])
    pwd1 = forms.CharField(max_length=16, min_length=6)
    pwd2 = forms.CharField(max_length=16, min_length=6)

    def clean_telephone(self):
        telephone = self.cleaned_data.get('telephone')
        exists = User.objects.filter(telephone=telephone).exists()
        if exists:
            raise forms.ValidationError(message="%s已经被注册！" % telephone)
        return telephone

    def clean(self):
        cleaned_data = super().clean()
        pwd1 = self.cleaned_data.get('pwd1')
        pwd2 = self.cleaned_data.get('pwd2')
        if pwd1 != pwd2:
            raise forms.ValidationError(message='两次密码不一致')
        return cleaned_data
