"""practice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from core.views import frontpage, signup

from core.forms import UserLoginForm, ResetPasswordForm, NewPasswordForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('signup/', signup, name="signup"),
    path('login/', views.LoginView.as_view(template_name="login.html", authentication_form=UserLoginForm), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),

    path('password-reset/', views.PasswordResetView.as_view(template_name="reset_password.html", form_class=ResetPasswordForm), name="password_reset"),

    path('password-reset/done/', views.PasswordResetDoneView.as_view(template_name="reset_password_done.html"), name="password_reset_done"),

    path('password-reset-confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(template_name="reset_password_confirm.html", form_class=NewPasswordForm), name="password_reset_confirm"),

    path('password-reset-complete/', views.PasswordResetCompleteView.as_view(template_name="reset_password_complete.html"), name="password_reset_complete"),

]
