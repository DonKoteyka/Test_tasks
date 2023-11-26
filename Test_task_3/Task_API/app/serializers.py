from rest_framework import serializers

from app.models import Tasks


class TasksSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id', 'list', 'created_at', 'changed_at', 'completed']

