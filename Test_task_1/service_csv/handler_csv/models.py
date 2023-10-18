from django.db import models

# Create your models here.
class FileCSV(models.Model):
    file = models.FileField(blank=True)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.file

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'


