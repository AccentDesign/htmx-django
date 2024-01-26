from django.urls import path

from . import views

app_name = "files"
urlpatterns = [
    path("", views.file_list_results, name="file-list-results"),
    path(
        "<int:pk>/actions-trigger",
        views.file_actions_trigger,
        name="file-actions-trigger",
    ),
    path("<int:pk>/actions", views.file_actions, name="file-actions"),
    path("<int:pk>/action/delete", views.file_action_delete, name="file-action-delete"),
    path("upload", views.file_upload_form, name="file-upload"),
]
