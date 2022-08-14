from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("login/", LoginView.as_view(template_name="login/login.html"), name="login"),
    path(
        "logout/", LogoutView.as_view(template_name="login/logout.html"), name="logout"
    ),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name ='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name ='password_reset_complete'),
    path("", include("clientes.urls")),
    path("paquetes/", include("cuentas.urls")),
    


]
