from django.urls import path
from .views import (
  UserLoginView,
  UserRegisterView,
  UserLogoutView,

  PetugasLoginView,
  PetugasRegisterView,
  PetugasLogoutView,
)

urlpatterns = [
  path('login/', UserLoginView.as_view(), name="user_login"),
  path('register/', UserRegisterView.as_view(), name="user_register"),
  path('logout/', UserLogoutView.as_view(), name="user_logout"),

  path('petugas/login/', PetugasLoginView.as_view(), name='petugas_login'),
  path('petugas/register/', PetugasRegisterView.as_view(), name="petugas_register"),
  path('petugas/logout/', PetugasLogoutView.as_view(), name="petugas_logout"),
]