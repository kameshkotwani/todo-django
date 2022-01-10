from django.http.response import HttpResponse
from django.shortcuts import render

from django.views.generic import ListView

from base.models import Task

# Create your views here.
class TaskList(ListView):
  model = Task
  context_object_name = "tasks"