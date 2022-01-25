from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from medPal.profiles.forms import SignInForm


def sign_up(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign in')
    else:
        form = UserCreationForm()

    context = {
        'form': form,
    }
    return render(request, 'profiles/sing-up.html', context)


def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    else:
        form = SignInForm()

    context = {
        'form': form,
    }

    return render(request, 'profiles/sign-in.html', context)


@login_required
def sign_out(request):
    logout(request)
    return redirect('home')


# TODO: Add Forgoten Password https://ordinarycoders.com/blog/article/django-password-reset
