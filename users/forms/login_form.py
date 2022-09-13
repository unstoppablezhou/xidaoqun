from django import forms
from django.core.exceptions import ValidationError
from utils import encrypt
from users.forms.bootstrap_form import BootStrapForm


class LoginForm(BootStrapForm, forms.Form):
    email = forms.EmailField(label="邮箱")
    password = forms.CharField(label="密码",
                               min_length=8,
                               max_length=64,
                               error_messages={
                                   'min_length': '密码长度不能小于8个字符',
                                   'max_length': '密码长度不能大于64个字符'
                               },
                               widget=forms.PasswordInput())
    code = forms.CharField(label="图片验证码", widget=forms.TextInput())

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    def clean_password(self):
        pwd = self.cleaned_data['password']
        # 密码加密存储
        return encrypt.md5(pwd)

    def clean_code(self):
        """钩子 图片是否正确"""
        code = self.cleaned_data['code']
        session_code = self.request.session.get('image_code')
        print(session_code)
        if not session_code:
            raise ValidationError('验证码已过期，请重新获取')
        if code.strip().upper() != session_code.strip().upper():  # upper()支持小写，strip()去空格
            raise ValidationError('验证码输入错误')
        return code
