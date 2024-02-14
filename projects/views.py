from django.shortcuts import render
from .models import Project
from .forms import ProjectForm

def list_all_project(request):
    project_list = Project.objects.all()
    return render(request, 'projects/projects.html', {'project_list':project_list})


def get_project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/project.html', {'projectObj':projectObj})


def submit_form(request):
    formObj = ProjectForm()
    context = {'form': formObj}

    return render(request, 'projects/project_form.html', context=context)
