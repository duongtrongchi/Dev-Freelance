from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm

def list_all_project(request):
    project_list = Project.objects.all()
    return render(request, 'projects/projects.html', {'project_list':project_list})


def get_project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'projectObj':projectObj})

@login_required(login_url='login-page')
def create_project(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        print(request)
        if form.is_valid():
            form.save()
            return redirect('list_all_job')

    context = {'form': form}
    return render(request, 'projects/form-template.html', context=context)

@login_required(login_url='login-page')
def update_project(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('list_all_job')

    context = {'form': form}
    return render(request, 'projects/form-template.html', context=context)

@login_required(login_url='login-page')
def delete_project(request, pk):
    project = Project.objects.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('list_all_job')

    context = {'object': project}
    return render(request, 'projects/delete_form.html', context=context)