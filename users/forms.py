from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from users.models import User
class RegisterForm(forms.ModelForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Login', 'class': 'form-control w-100'}))
    email = forms.CharField(label="", widget=forms.EmailInput(attrs={'placeholder': 'Email kiriting', 'class': 'form-control w-100'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Parol', 'class': 'form-control w-100'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Parolni tasdiqlash', 'class': 'form-control w-100'}))
    first_name = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Ism kiriting', 'class': 'form-control w-100'}))
    last_name = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Familiyangizni kiriting', 'class': 'form-control w-100'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'first_name', 'last_name']

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2!=password:
            raise forms.ValidationError("Passwords don't match")
        return password
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username)<2 or len(username)>30:
            raise forms.ValidationError("Username 5 va 30 orasida bo'lishi kerak")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Bunday email bazada mavjud")
        return email

class LoginForm(forms.Form):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control w-100'}))
    password = forms.CharField(label="",widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control w-100'}))
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username)<5 or len(username)>30:
            raise forms.ValidationError("Username 5 va 30 orasida bo'lishi kerak")
        return username
    
class ProfileUpdateForm(forms.ModelForm):
    username = forms.CharField(disabled=True, label="Login", widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control w-100'}))
    first_name = forms.CharField(label="Ismingiz", widget=forms.TextInput(attrs={'placeholder': 'Ismingiz', 'class': 'form-control w-100'}))
    last_name = forms.CharField(label="Familiyangiz", widget=forms.TextInput(attrs={'placeholder': 'Familiyangiz', 'class': 'form-control w-100'}))
    email = forms.CharField(disabled=True, label="Email", widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control w-100'}))
    image = forms.ImageField(label="Rasm", widget=forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Rasm'}))
    phone_number = forms.CharField(label="Telefon raqamingiz", widget=forms.TextInput(attrs={'placeholder': 'Telefon raqamingiz', 'class': 'form-control w-100'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', "email", 'image','phone_number']


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Eski parolingiz', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='Yangi parol', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Parolni tasdiqlang', widget=forms.PasswordInput)

    def clean_new_password2(self):
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.cleaned_data.get('new_password2')

        if new_password1 and new_password2 and new_password1 != new_password2:
            raise forms.ValidationError("Yangi parollar mos kelmadi. Iltimos, qaytadan kiriting.")
        
        return new_password2