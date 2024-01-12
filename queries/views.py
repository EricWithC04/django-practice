from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Project, Task

# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>")

def about(request):
    return HttpResponse("<h1>About</h1>")

def main(request):
    return HttpResponse("<h1>Main</h1>")

def user(request, user_id):
    return HttpResponse(f"<h1>Hello {user_id}!</h1>")

def get_all_projects(request):
    all_projects = list(Project.objects.values())
    return JsonResponse(all_projects, safe=False)

def get_all_tasks(request):
    all_tasks = list(Task.objects.values())
    return JsonResponse(all_tasks, safe=False)

def task_by_id(request, id):
    task = get_object_or_404(Task, id=id)
    return HttpResponse(f"task: {task.title}")