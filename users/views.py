from django.shortcuts import render
from .models import Profile


def profiles(request):
    list_profiles = Profile.objects.all()
    return render(request, 'users/profiles.html', {'profiles':list_profiles})


def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)

    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")

    context = {'profile': profile, 'topSkills': topSkills, 'otherSkills':otherSkills}
    return render(request, 'users/user-profile.html', context=context)



