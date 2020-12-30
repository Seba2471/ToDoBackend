from django_filters.rest_framework import DjangoFilterBackend

from .models import Task,TaskList
from .serializers import TaskSerializers,TaskListSerializers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class TaskListViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskListSerializers
    queryset = TaskList.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']

class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializers
    queryset = Task.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['list']
