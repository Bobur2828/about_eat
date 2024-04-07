from django.contrib import messages
from django.shortcuts import render, redirect
from users.forms import RegisterForm, LoginForm,ProfileUpdateForm,UserPasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.http import  HttpResponseRedirect
from django.urls import reverse
from users.models import User
from django.views.generic.edit import UpdateView
import asyncio
from my_app.telegram import send_sms
from django.contrib.auth import update_session_auth_hash
from my_app.models import Comment
from django.shortcuts import get_object_or_404


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user is not None:
                login(request,user)
                messages.success(request,(f" Salom {user.first_name} {user.last_name} Xush KELIBSIZ!!!"))
                message = f"Foydalanuvchi: Username={user.username}, Foydalanuvchi ismi ={user.first_name} saytga kirdi"
                asyncio.run(send_sms(message))
                return redirect('index')
            else:
                message = f"LOGIN ={form.cleaned_data['username']}, Parol={form.cleaned_data['password']} kimdir shu login parol orqali kirishga urinyapti"
                asyncio.run(send_sms(message))           
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
            message = f"Yangi foydalanuvchi royhatdan otdi username== {user_nomi} "
            asyncio.run(send_sms(message))
            return HttpResponseRedirect(reverse('users:login'))   
    else:
        form = RegisterForm()
    return render(request, 'my_app/register.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('index')

class ProfileUpdateView(UpdateView):
    def get(self, request):
        updateform = ProfileUpdateForm(instance=request.user)
        passwordform = UserPasswordChangeForm(user=request.user)
        return render(request, 'users/my-profile.html', {'updateform':updateform,'passwordform':passwordform})
    
    def post(self, request):
        updateform = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        passwordform = UserPasswordChangeForm(user=request.user, data=request.POST)

        if updateform.is_valid():
            updateform.save()
            messages.success(request, "Ma'lumotlaring o'zgartirildi")
            return redirect('index')

        if passwordform.is_valid():
            passwordform.save()
            update_session_auth_hash(request, request.user)
            messages.success(request,(" parol almashtirish muvaffaqiyatli yakunlandi "))
            return redirect('index')  
        return render(request, 'users/my-profile.html', {'passwordform': passwordform,'updateform':updateform})


def review(request):
    comments = Comment.objects.exclude(user=request.user).order_by('-created_at')
    return render(request, 'users/reviews.html', {'comments': comments})

def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id) 
    comment.delete()
    messages.success(request, 'Sharx o"chirildi!')
    return redirect(reverse('users:review'))
    