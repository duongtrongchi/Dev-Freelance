from django.urls import path
from .views import list_all_project, get_project, submit_form

urlpatterns = [
    path('', list_all_project, name='list_all_job'),
    path('project/<str:pk>', get_project, name='get_project'),
    path('create-project/', submit_form, name='submit-form')
]