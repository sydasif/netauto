from django.urls import path

from .views import login_view, logout_view, profile, register

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
]
