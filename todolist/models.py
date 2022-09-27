from datetime import datetime
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ToDoList(models.Model):
    user = models.ForeignKey(
           User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.BooleanField(default=False)