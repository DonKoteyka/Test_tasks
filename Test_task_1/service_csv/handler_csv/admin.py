from django.contrib import admin

from handler_csv.models import FileCSV


# Register your models here.
@admin.register(FileCSV)
class FileCSVAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'created_at',)
