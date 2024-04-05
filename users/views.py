from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from users.forms import RegisterForm, LoginForm,ProfileUpdateForm
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from users.models import User
from django.views.generic.edit import UpdateView
import asyncio
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user is not None:
                login(request,user)
                messages.success(request,(f" Salom {user.first_name} {user.last_name} sizni yana ko'rib turganimizdan hursandmiz"))
                message = f"Foydalanuvchi: Username={user.username}, Foydalanuvchi ismi ={user.first_name} saytga kirdi"
                return redirect('index')
            else:
                messages.error(request,("Login yoki parolni notogri kiritdingiz  iltimos qayta urinib koring "))
    else:
        form = LoginForm()
    return render(request,'my_app/login.html',{'form':form})


def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user_nomi=form.cleaned_data['username']
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request,(" Ro'yhatdan o'tish muvaffaqiyatli yakunlandi "))
            message = f"Yangi foydalanuvchi royhatdan otdi username== {user_nomi} "
            return HttpResponseRedirect(reverse('users:login'))   
    else:
        form = RegisterForm()
    return render(request, 'my_app/register.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('index')

from django.shortcuts import get_object_or_404



class ProfileUpdateView(UpdateView):

    def get(self, request):
        form = ProfileUpdateForm(instance=request.user)
        return render(request, 'account_update.html', {'form':form})
    def post(self, request):
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        r = request.POST
        f = request.FILES
        print(r)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
        return render(request, 'account_update.html', {'form':form})

class Profile(View):
    def get(self, request):
        return render(request, 'account_view.html')
    