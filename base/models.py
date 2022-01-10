from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
  # Contains a user Model
  user  = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
  
  # title of the task
  title = models.CharField(max_length=50)

  # description of the task, will remove later
  description = models.TextField(max_length=100,blank=True,null=True)
  
  # wether completed or not
  complete = models.BooleanField(default=False)

  # time created
  created = models.DateTimeField(auto_now_add=True)
  
  # returns the tile of the task at the homepage
  def __str__(self) -> str:
      return self.title

  # returns the ordering of the columns
  class Meta:
    ordering = ["complete"]

