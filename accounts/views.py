from django.shortcuts import render, redirect
from .form import SignupForm
from django.urls import reverse
from django.contrib.auth import authenticate, login
from pip._vendor.urllib3 import request

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
