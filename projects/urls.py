from django.urls import path
from .views import list_all_project, get_project, create_project, update_project, delete_project

urlpatterns = [
    path('', list_all_project, name='list_all_job'),
    path('project/<str:pk>', get_project, name='single_project'),
    path('create-project/', create_project, name='create_project'),
    path('update-project/<str:pk>', update_project, name='update_a_project'),
    path('delete-project/<str:pk>', delete_project, name='delete-project')
]