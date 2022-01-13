from django.http.response import HttpResponse
from django.shortcuts import render

from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView
from base.models import Task
from django.urls import reverse_lazy

# Create your views here.
class TaskList(ListView):
  model = Task
  context_object_name = "tasks"

class TaskDetail(DetailView):
  model = Task
  context_object_name = "task"
  template_name = "base/task.html"

class TaskCreate(CreateView):
  model = Task
  fields = '__all__'
  success_url = reverse_lazy('tasks')

