from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView


class Login(LoginView):
    template_name = "login.html"
    next_page = reverse_lazy("home")
    success_message = "You are logged in successfully"
