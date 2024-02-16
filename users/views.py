from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile


def login_user(request):

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'Tài khoản không tồn tại!')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Đăng nhập thành công!')
            return redirect('profiles')
        else:
            messages.error(request, 'Username or password không chính xác!')

    return render(request, 'users/login_register.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'Đăng xuất thành công!')
    return redirect('profiles')


def profiles(request):
    list_profiles = Profile.objects.all()
    return render(request, 'users/profiles.html', {'profiles':list_profiles})


def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)

    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")

    context = {'profile': profile, 'topSkills': topSkills, 'otherSkills':otherSkills}
    return render(request, 'users/user-profile.html', context=context)



