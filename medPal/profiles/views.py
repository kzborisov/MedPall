from django.contrib.auth import logout, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView

from medPal import settings
from medPal.profiles.forms import SignInForm

UserModel = get_user_model()


class SignUpView(CreateView):
    template_name = 'profiles/sing-up.html'
    model = UserModel
    form_class = UserCreationForm
    success_url = reverse_lazy('sign in')


class SignInView(LoginView):
    template_name = 'profiles/sign-in.html'
    form_class = SignInForm

    def get_success_url(self):
        return reverse('home')


class LogoutView(LoginRequiredMixin, View):
    @staticmethod
    def get(request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)

# TODO: Add Forgoten Password https://ordinarycoders.com/blog/article/django-password-reset
