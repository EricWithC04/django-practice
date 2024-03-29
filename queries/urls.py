from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.hello),
    path('about', views.about),
    path('', views.main),
    path('user/<int:user_id>', views.user),
    path('projects', views.get_all_projects),
    path('create_project', views.create_project),
    path('project/<int:project_id>', views.project_details),
    path('tasks', views.get_all_tasks),
    path('task_by_id/<int:id>', views.task_by_id),
    path('new_task', views.new_task),
]