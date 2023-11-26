from django_filters import rest_framework as filters

from app.models import Tasks


class TasksFilter(filters.FilterSet):

    class Meta:
        model = Tasks
        fields = ['id', 'list', 'created_at', 'changed_at', 'completed']
