from typing import Any
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from django.http import HttpResponseRedirect
from django.contrib.auth.views import (
  LoginView,
  LogoutView
)
from masyarakat_view.models import (
  Masyarakat,
)
from petugas_view.models import (
  Petugas
)

from .forms import (
  MasyarakatLoginForm,
  MasyarakatCreationForm,
  PetugasCreationForm,
  PetugasLoginForm,
)

class UserLoginView(LoginView):
  model = Masyarakat
  form_class = MasyarakatLoginForm
  template_name = 'auth/user_login.html'

  def get(self, request):
    if self.request.user.is_authenticated:
      user = self.request.user
      if isinstance(user, Masyarakat):
        return redirect('masyarakat:user_dashboard')
      else:
        return redirect('petugas:petugas_dashboard')
    return super().get(request)

  def get_success_url(self):
    return reverse_lazy('masyarakat:user_dashboard')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['judul'] = 'Login Page'
    return context

class UserRegisterView(CreateView):
  form_class = MasyarakatCreationForm
  template_name = 'auth/user_register.html'

  def get(self, request):
    if self.request.user.is_authenticated:
      user = self.request.user
      if isinstance(user, Masyarakat):
        return redirect('masyarakat:user_dashboard')
      else:
        return redirect('petugas:petugas_dashboard')
    return super().get(request)

  def get_success_url(self):
    return reverse_lazy('auth:user_login')

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["judul"] = "Register Page"
      return context

class UserLogoutView(LogoutView):
  model = Masyarakat

  def get_success_url(self):
      return reverse_lazy('auth:user_login')

class PetugasLoginView(LoginView):
    template_name = 'auth/petugas_login.html'

    def get(self, request):
      if self.request.user.is_authenticated:
        return redirect('petugas:petugas_dashboard')
      
      user = self.request.user
      if isinstance(user, Masyarakat):
        return redirect('masyarakat:user_dashboard')
      return super().get(request)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["judul"] = "Login Petugas Page"
        return context

    def form_valid(self, form):
        user = form.get_user()
        if not isinstance(user, Petugas):
            form.add_error(None, "Akun ini tidak valid untuk login sebagai petugas.")
            return self.form_invalid(form)
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        if self.request.user.level == 'admin':
            return reverse_lazy('petugas:petugas_dashboard')
        return reverse_lazy('petugas:petugas_dashboard')

class PetugasRegisterView(CreateView):
  model = Petugas
  form_class = PetugasCreationForm
  template_name = 'auth/petugas_register.html'

  def get(self, request):
      if self.request.user.is_authenticated:
        return redirect('petugas:petugas_dashboard')
      
      user = self.request.user
      if isinstance(user, Masyarakat):
        return redirect('masyarakat:user_dashboard')
      return super().get(request)

  def get_success_url(self):
    return reverse_lazy('auth:petugas_login')

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["judul"] = "Register Petugas Page"
      return context
  
class PetugasLogoutView(LogoutView):
  model = Petugas

  def get_success_url(self):
    return reverse_lazy('auth:petugas_login')