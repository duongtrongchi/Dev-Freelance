from django.urls import path
from .views import list_all_project, get_project

urlpatterns = [
    path('', list_all_project, name='list_all_job'),
    path('project/<str:pk>', get_project, name='get_project')
]