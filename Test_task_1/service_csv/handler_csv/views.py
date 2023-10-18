from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from handler_csv.forms import FileCSVForm
from handler_csv.models import FileCSV
from handler_csv.parser_csv import ViewCSV




def index(request):
    return redirect('home')


# Create your views here.
def get_list_files(request):
    template = 'home.html'
    files_csv = FileCSV.objects.all()
    object_list = list()
    for i in files_csv:
        k = ViewCSV(i.file)
        k.id = i.id
        object_list.append(k)

    context = {'object_list': object_list}

    return render(request, template, context)


def get_one_file(request, pk):
    tpe_srt = request.GET.get("sort")
    file_name = FileCSV.objects.filter(id=pk)[0]
    file_content = ViewCSV(file_name.file)
    file_content.created_at = file_name.created_at
    file_content.sort(tpe_srt)
    context = {
        'file': file_content
    }
    return render(request, 'tab.html', context)


def load_data(request):
    if request.method == "POST":
        form = FileCSVForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FileCSVForm()
    return render(request, "upload.html", {"form": form})


    # if request.method == "POST":
    #     uploaded_file = request.FILES["sheet"]
    #     fs = FileSystemStorage()
    #     fs.save(uploaded_file.name, uploaded_file)
    #
    # return render(request, "upload.html", )
