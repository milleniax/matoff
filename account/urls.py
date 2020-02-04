from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import User_Auth


urlpatterns = [
    path('', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(authentication_form=User_Auth), name='login'),
    path('registration',views.register, name='register'),
    path('password_reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    
]
