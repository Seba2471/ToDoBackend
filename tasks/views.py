from django_filters.rest_framework import DjangoFilterBackend

from .models import Task
from .serializers import TaskSerializers
from rest_framework import viewsets


# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializers
    queryset = Task.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Title']