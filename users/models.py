from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import uuid

class Profile(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )
    created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=1024, null=True, blank=True)
    short_intro = models.CharField(max_length=2048, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    headline = models.CharField(max_length=2048, null=True, blank=True)
    bio = models.CharField(max_length=2048, null=True, blank=True)
    location = models.CharField(max_length=2048, null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, default='default.jpeg')
    social_github = models.CharField(max_length=2048, null=True, blank=True)
    social_twitter = models.CharField(max_length=2048, null=True, blank=True)
    social_linkedin = models.CharField(max_length=2048, null=True, blank=True)
    social_website = models.CharField(max_length=2048, null=True, blank=True)
    social_youtube = models.CharField(max_length=2048, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Skill(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=1024, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            name=user.first_name
        )
        

post_save.connect(createProfile, sender=User)