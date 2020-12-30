from rest_framework import serializers
from .models import Task,TaskList

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskListSerializers(serializers.ModelSerializer):
    class Meta:
        model = TaskList
        fields = '__all__'