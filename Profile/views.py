from django.shortcuts import render, redirect
from User.models import CustomUser
from Profile.forms import ProfileChangeForm


def islogged(func):
    def wrapper(request):
        if request.user.is_anonymous:
            return redirect('/')
        func(request)
    return wrapper


def profile_view(request, username):
    profile = CustomUser.objects.filter(username=username).first()
    if profile == None:
        return redirect('/')

    if request.method == 'GET':
        form = ProfileChangeForm
        return render(request, 'profile.html', context={
            'profile': profile, 
            'form': form, 
            'user': None if request.user.is_anonymous else request.user
            })

    if request.method == 'POST':
        form = ProfileChangeForm(data=request.POST)
        if form.is_valid():
            print('qq'+form.cleaned_data.get('name'))
            if form.cleaned_data.get('email') != None:
                profile.email = form.cleaned_data.get('email')
            if form.cleaned_data.get('name') != '':
                profile.name = form.cleaned_data.get('name')
            if form.cleaned_data.get('username') != '':
                profile.username = form.cleaned_data.get('username')
            if form.cleaned_data.get('phone') != None:
                profile.phone = form.cleaned_data.get('phone')
            profile.save()

        return redirect('/')
