from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Project, Task

# Create your views here.
def hello(request):
    return render(request, "hello.html")

def about(request):
    username = "EricWithC04"
    return render(request, "about.html", {
        "username": username,
    })

def main(request):
    return render(request, "main.html")

def new_task(request):
    return render(request, "create_tasks.html")

def user(request, user_id):
    return HttpResponse(f"<h1>Hello {user_id}!</h1>")

def get_all_projects(request):
    all_projects = Project.objects.all()
    return render(request, "projects.html", {
        "projects": all_projects
    })

def get_all_tasks(request):
    all_tasks = Task.objects.all()
    return render(request, "tasks.html", {
        "tasks": all_tasks
    })

def task_by_id(request, id):
    task = get_object_or_404(Task, id=id)
    return HttpResponse(f"task: {task.title}")