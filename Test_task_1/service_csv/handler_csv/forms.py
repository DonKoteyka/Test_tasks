from django.forms import ModelForm

from handler_csv.models import FileCSV


class FileCSVForm(ModelForm):
    class Meta:
        model = FileCSV
        fields = ['file',]
