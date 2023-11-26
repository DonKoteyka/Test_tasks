from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from app.models import Tasks
from app.serializers import TasksSerialazer
from app.filters import TasksFilter


class TasksViewSet(ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerialazer
    filterset_class = TasksFilter
