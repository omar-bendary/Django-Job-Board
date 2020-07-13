from django.shortcuts import render, redirect
from .form import SignupForm, ProfileForm, UserForm
from django.urls import reverse
from django.contrib.auth import authenticate, login
from pip._vendor.urllib3 import request
from .models import Profile
# Create your views here.


def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('accounts/profile')

    context = {

        'form': form

    }
    return render(request, 'registration/signup.html', context)


def profile(request):
    profile = Profile.objects.get(user=request.user)

    context = {
        'profile': profile
    }
    return render(request, 'profile.html', context)


def profile_edit(request):

    profile = Profile.objects.get(user=request.user)
    profileform = ProfileForm(instance=profile)
    userform = UserForm(instance=request.user)

    if request.method == 'POST':
        profileform = ProfileForm(
            request.POST, request.FILES, instance=profile)

        userform = UserForm(request.POST, instance=request.user)
        if profileform.is_valid() and userform.is_valid():
            profileform.save()
            userform.save()
            return redirect('accounts:profile')

    context = {
        'profileform': profileform,
        'userform': userform
    }

    return render(request, 'profile_edit.html', context)
