from django import forms
from django.core.exceptions import ValidationError
from utils import encrypt
from users import models


class RegisterModelForm(forms.ModelForm):
    # passWord = forms.CharField(label="密码", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请输入密码'}))

    password = forms.CharField(label="密码",
                               min_length=8,
                               max_length=64,
                               error_messages={
                                   'min_length': '密码长度不能小于8个字符',
                                   'max_length': '密码长度不能大于64个字符'
                               },
                               widget=forms.PasswordInput())
    confirm_password = forms.CharField(label="重复密码",
                                       min_length=8,
                                       max_length=64,
                                       error_messages={
                                           'min_length': '密码长度不能小于8个字符',
                                           'max_length': '密码长度不能大于64个字符'
                                       },
                                       widget=forms.PasswordInput)

    # code = forms.CharField(label="验证码")

    class Meta:
        model = models.UsersInfo
        fields = ['email', 'username', 'password', 'confirm_password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = '请输入%s' % (field.label,)

    def clean_email(self):
        email = self.cleaned_data['email']  # cleaned_data['email']只能拿到前面的值，如['username', 'email']
        exists = models.UsersInfo.objects.filter(email=email).exists()
        if exists:
            raise ValidationError('邮箱已存在')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        exists = models.UsersInfo.objects.filter(username=username).exists()
        if exists:
            raise ValidationError('用户名已存在')
        return username

    def clean_password(self):
        pwd = self.cleaned_data['password']
        # 密码加密存储
        return encrypt.md5(pwd)

    def clean_confirm_password(self):
        pwd = self.cleaned_data['password']
        confirm_pwd = encrypt.md5(self.cleaned_data['confirm_password'])
        if pwd != confirm_pwd:
            raise ValidationError('两次密码不一致')
        return confirm_pwd
