from django import forms
from .models import Project

class CreateNewTask(forms.Form):
    all_projects = Project.objects.all()
    options = [("", "Seleccionar")]

    options.extend([(project.id, project.name) for project in all_projects])

    title = forms.CharField(label="Titulo de la tarea", max_length=200, widget=forms.TextInput(attrs={'class': 'form-input'}))
    description = forms.CharField(label="Descripcion de la tarea", widget=forms.Textarea(attrs={'class': 'form-input'}))
    project = forms.ChoiceField(label="Proyecto", widget=forms.Select, choices=options)

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del proyecto", max_length=200, widget=forms.TextInput(attrs={'class': 'form-input'}))