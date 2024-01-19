from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject

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
    if request.method == "GET":
        return render(request, "tasks/create_tasks.html", {
        "form": CreateNewTask()
    })
    elif request.method == "POST":
        Task.objects.create(
            title = request.POST["title"],
            description = request.POST["description"],
            project_id = 1
        )
        return redirect("/tasks")
    

def create_project(request):
    if request.method == "GET":
        return render(request, "projects/create_project.html", {
            "form": CreateNewProject()
        })
    elif request.method == "POST":
        Project.objects.create(
            name = request.POST["name"]
        )
        return redirect("/projects")

def project_details(request, project_id):
    detail_project = get_object_or_404(Project, id=project_id)
    task_of_project = Task.objects.filter(project_id=project_id)
    return render(request, "projects/project_details.html", {
        "detail": detail_project,
        "tasks": task_of_project
    })

def user(request, user_id):
    return HttpResponse(f"<h1>Hello {user_id}!</h1>")

def get_all_projects(request):
    all_projects = Project.objects.all()
    return render(request, "projects/projects.html", {
        "projects": all_projects
    })

def get_all_tasks(request):
    all_tasks = Task.objects.all()
    return render(request, "tasks/tasks.html", {
        "tasks": all_tasks
    })

def task_by_id(request, id):
    task = get_object_or_404(Task, id=id)
    return HttpResponse(f"task: {task.title}")