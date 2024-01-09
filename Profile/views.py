from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from User.models import CustomUser
from Profile.models import PostModel
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


def post_view(request, id, username):
    post = PostModel.objects.get(id=id)
    user = None if request.user.is_anonymous else request.user

    if request.method == 'GET':
        return render(request, 'post.html', context={
            'user': user,
            'post': post,
        })
    if request.method == 'POST':
        reposted = post.reposted
        liked = post.liked
        saved = post.saved
        if 'Like' in request.POST:
            liked.add(user)
        elif 'Remove like' in request.POST:
            liked.remove(user)
        
        if 'Repost' in request.POST:
            reposted.add(user)
        elif 'Remove repost' in request.POST:
            reposted.remove(user)
            
        if 'Save' in request.POST:
            saved.add(user)
        elif 'Remove save' in request.POST:
            saved.remove(user)
            
        return HttpResponseRedirect(reverse('post-view', args=[username, id]))
