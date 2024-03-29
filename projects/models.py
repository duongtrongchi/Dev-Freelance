from django.db import models
from users.models import Profile
import uuid


class Project(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    feature_image = models.ImageField(null=True, blank=True, default='default.jpeg')
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    ratio_total = models.IntegerField(default=0, null=True, blank=True)
    demo_link = models.CharField(max_length=2048, null=True, blank=True)
    source_link = models.CharField(max_length=2048, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.title


class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote')
    )
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )
    # owner =
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value =  models.CharField(max_length=2048, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.value


class Tag(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.name
