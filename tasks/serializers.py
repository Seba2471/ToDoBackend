from rest_framework import serializers
from .models import Task,TaskList

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskListSerializers(serializers.ModelSerializer):

    done = serializers.SerializerMethodField()
    all = serializers.SerializerMethodField()

    class Meta:
        model = TaskList
        fields = '__all__'

    # Zlicza wszystkie taski dla podanej listy
    def get_all(self,obj):
        obj.all = Task.objects.filter(list=obj.id).count()
        return obj.all

    # Zlicza wykonane taski dla podanej listy
    def get_done(self,obj):
        obj.done = Task.objects.filter(done=True,list=obj.id).count()
        return obj.done