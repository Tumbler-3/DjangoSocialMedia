from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.hashers import make_password
from User.forms import CustomUserRegistrtionForm, CustomUserLoginForm
from User.models import CustomUser

def logout_view(request):
    logout(request)
    return redirect('/')
    
def main(request):
    return render(request, 'index.html', context={'user': None if request.user.is_anonymous else request.user})


def registartion_view(request):
    if request.method == 'GET':
        registartion_form = CustomUserRegistrtionForm
        return render(request, 'reg.html', context={
            'user': None if request.user.is_anonymous else request.user,
            'registartion_form': registartion_form,
        })
    
    if request.method == 'POST':
        registartion_form = CustomUserRegistrtionForm(data=request.POST)
        
        if registartion_form.is_valid():
            user = CustomUser.objects.create(
                username = registartion_form.cleaned_data.get('username'),
                email = registartion_form.cleaned_data.get('email'),
                name = registartion_form.cleaned_data.get('name'),
            )
            user.set_password(registartion_form.cleaned_data.get('password1'))
            user.save()
            return redirect('/')
        
        return render(request, 'reg.html', context={
            'user': None if request.user.is_anonymous else request.user,
            'registartion_form': registartion_form,
        })


def login_view(request):
    if request.method == 'GET':
        login_form = CustomUserLoginForm
        return render(request, 'login.html', context={
            'user': None if request.user.is_anonymous else request.user,
            'login_form': login_form,
        })
    
    if request.method == 'POST':
        login_form = CustomUserLoginForm(data=request.POST)
        
        if login_form.is_valid():
            user = authenticate(
                username = login_form.cleaned_data.get('username'),
                password = login_form.cleaned_data.get('password')
            )
            if user:
                login(request, user=user)
                return redirect('/')
            else:
                login_form.add_error('username', 'username or password is incorrect')
        return render(request, 'login.html', context={
            'user': None if request.user.is_anonymous else request.user,
            'login_form': login_form,
        })