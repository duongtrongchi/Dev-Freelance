from django.urls import path
from .views import (
    user_profile,
    profiles,
    login_user,
    logout_user,
    register_user,
    user_account,
    editAccount,
    updateSkill
)


urlpatterns = [
    path('login/', login_user, name="login-page"),
    path('logout/', logout_user, name="logout-page"),
    path('register/', register_user, name="register-page"),

    path('account/', user_account, name="user-account"),
    path('edit-account', editAccount, name="edit-account"),

    path('update-skills/<str:pk>', updateSkill, name="update-skills"),

    path('profile/<str:pk>', user_profile, name='user-profile'),
    path('', profiles, name='profiles'),
]