from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, ProfileForm, SkillForm
from .models import Profile


def login_user(request):
    page = 'login'

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

    return render(request, 'users/login_register.html', {'page': page})


def logout_user(request):
    logout(request)
    messages.success(request, 'Đăng xuất thành công!')
    return redirect('profiles')


def register_user(request):
    page = 'register'
    form = CustomUserCreationForm()
    context = {'page': page, 'form':form}

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'Tạo tài khoản thành công!')

            login(request, user)
            return redirect('profiles')
    else:
        messages.error(request, 'Tạo tài khoản thất bại!')

    return render(request, 'users/login_register.html', context=context)


def profiles(request):
    list_profiles = Profile.objects.all()
    return render(request, 'users/profiles.html', {'profiles':list_profiles})


def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)

    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")

    context = {'profile': profile, 'topSkills': topSkills, 'otherSkills':otherSkills}
    return render(request, 'users/user-profile.html', context=context)


def user_account(request):

    profile = request.user.profile

    skills = profile.skill_set.all()
    projects = profile.project_set.all()


    context = {'profile': profile, 'skills':skills, 'projects':projects}
    return render(request, 'users/account.html', context=context)



def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('user-account')

    context = {"form": form}
    return render(request, 'users/profile_form.html', context=context)


def updateSkill(request, pk):
    profile = request.user.profile
    skills = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skills)


    if request.method == "POST":
        form = SkillForm(request.POST, instance=skills)
        if form.is_valid():
            form.save()

            return redirect("user-account")

    context = {"form": form}
    return render(request, "users/skills_form.html", context=context)

