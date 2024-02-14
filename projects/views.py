from django.shortcuts import render
from .models import Project


def list_all_project(request):
    project_list = Project.objects.all()
    return render(request, 'projects/projects.html', {'project_list':project_list})


def get_project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/project.html', {'projectObj':projectObj})
