from django.conf import settings
from django.db import models

import uuid


class Tasks(models.Model):
    list = models.TextField(blank=False)
    # uuid = models.UUIDField(
    #     default=uuid.uuid4,
    #     editable=False,
    #     unique=True
    # )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    changed_at = models.DateTimeField(
        auto_now=True
    )
    completed = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return f'ID: {self.id} Список: {self.list}'
