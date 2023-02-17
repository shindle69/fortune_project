# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from accounts.models import MyUser
 
# 회원 가입 폼
class RegistrationForm(UserCreationForm):
    
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')
 
    class Meta:
        model = MyUser
        fields = ('email', 'username', 'name', 'password1', 'password2', )
 
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = Account.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"Email {email} is already in use.")
 
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = MyUser.objects.get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"UserID {username} is already in use.")
 
 
 
# 로그인 인증 폼
class AccountAuthForm(forms.ModelForm):
    username = forms.CharField(label='Username', widget=forms.TextInput)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
 
    class Meta:
        model = MyUser
        fields = ('username', 'password')
 
    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError("Invalid login")
 
