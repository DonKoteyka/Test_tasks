from django.db import models

# Create your models here.
class FileCSV(models.Model):
    name = models.CharField(max_length=256, blank=True)
    file = models.FileField(upload_to='documents/', blank=True)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'


