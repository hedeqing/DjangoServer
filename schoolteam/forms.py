# from captcha.fields import CaptchaField
from django import  forms

class UserForm(forms.Form):
    number = forms.CharField(label="电话号码",max_length=128,widget=forms.TextInput(attrs={'class':"form-control",
            "placeholder":"number","autofocus":""}))
    password= forms.CharField(label="密码",max_length=256,widget=forms.PasswordInput(attrs ={'class':"form-control",
            "placeholder":"password"}))
    # captcha = CaptchaField(label="验证码")

class RegisterForm(forms.Form):

    gender = (
        ("male","男"),
        ("femal","女"),
    )

    name = forms.CharField(label="用户名",max_length=128,widget=forms.TextInput(attrs={'class':"form-control"}))
    password1 = forms.CharField(label="密码",max_length=256,widget=forms.PasswordInput(attrs={'class':"form-control"}))
    password2 = forms.CharField(label="确认密码",max_length=256,widget=forms.PasswordInput(attrs={'class':"form-control"}))
    dynamic = forms.CharField(label='动态',max_length=256,widget=forms.TextInput(attrs={'class':"form-control"}))
    sex = forms.ChoiceField(label = "性别",choices= gender)
    number = forms.CharField(label="电话号码", max_length=128, widget=forms.TextInput(attrs={'class': "form-control"}))
    picture = forms.ImageField(label="头像")



