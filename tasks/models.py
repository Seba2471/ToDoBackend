from django.db import models


# Create your models here.

class Task(models.Model):
    Title = models.CharField(max_length=140)
    name = models.CharField(max_length=140)
    done = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['Title']
