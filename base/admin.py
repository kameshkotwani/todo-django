from django.contrib import admin
from .models import Task

# registering the model with admin panel
admin.site.register(Task)

