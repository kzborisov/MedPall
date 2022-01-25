from django.urls import path

from medPal.profiles.views import SignUpView, SignInView, LogoutView

urlpatterns = [
    path('sign-up', SignUpView.as_view(), name="sign up"),
    path('sign-in', SignInView.as_view(), name="sign in"),
    path('sign-out', LogoutView.as_view(), name="sign out"),
]
