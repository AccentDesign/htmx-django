from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from files.forms import FileForm
from files.models import File


def file_list_results(request):
    files = File.objects.all()
    return render(request, "files/file-list-results.html", {"files": files})


def file_actions(request, pk: int):
    file = get_object_or_404(File, pk=pk)
    return render(request, "files/file-actions.html", {"file": file})


def file_actions_trigger(request, pk: int):
    file = get_object_or_404(File, pk=pk)
    return render(request, "files/file-actions-trigger.html", {"file": file})


def file_action_delete(request, pk: int):
    file = get_object_or_404(File, pk=pk)
    if "confirm" in request.POST:
        file.delete()
        return HttpResponse(headers={"HX-Trigger-After-Settle": "fileList"})
    return render(request, "files/file-action-delete.html", {"file": file})


def file_upload_form(request):
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            response = render(request, "files/file-upload-success.html")
            response["HX-Trigger-After-Settle"] = "fileList"
            return response
    else:
        form = FileForm()
    return render(request, "files/file-upload-form.html", {"form": form})
