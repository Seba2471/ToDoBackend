from django.db import models
from django.db.models import Count

# Create your models here.

class TaskList(models.Model):
    name = models.CharField(max_length=140)
    description = models.CharField(max_length=140, blank=True, null=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=140)
    done = models.BooleanField()
    list =  models.ForeignKey(TaskList,related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
