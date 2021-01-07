from django_filters.rest_framework import DjangoFilterBackend
from .models import Task, TaskList
from .serializers import TaskSerializers, TaskListSerializers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count


# Create your views here.

class TaskListViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    serializer_class = TaskListSerializers
    queryset = TaskList.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']

    @action(detail=True)
    def size_Task(self, request, pk=None):
        done = Task.objects.filter(done=True, list=pk).count()
        all = Task.objects.filter(list=pk).count()
        data = [{"done": done, "all": all}]
        return Response(data, status=status.HTTP_200_OK)


class TaskViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializers
    queryset = Task.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['list']
