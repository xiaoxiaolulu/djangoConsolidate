from django import forms


class MessageBoardForm(forms.Form):

    title = forms.CharField(max_length=100, min_length=2, label="标题")
    content = forms.CharField(widget=forms.Textarea, label='内容')
    email = forms.EmailField(label='邮箱')
    replay = forms.BooleanField(required=False, label='回复')
