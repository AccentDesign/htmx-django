from django.urls import path

from . import views

app_name = "inquiries"
urlpatterns = [
    path("form", views.inquiry_form, name="form"),
]
