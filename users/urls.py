from django.urls import path
from .views import (
    user_profile,
    profiles,
    login_user,
    logout_user,
    register_user
)


urlpatterns = [
    path('login/', login_user, name="login-page"),
    path('logout/', logout_user, name="logout-page"),
    path('register/', register_user, name="register-page"),

    path('profile/<str:pk>', user_profile, name='user-profile'),
    path('', profiles, name='profiles'),
]