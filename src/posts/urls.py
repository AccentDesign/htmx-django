from django.urls import path

from . import views

app_name = "posts"
urlpatterns = [
    path("latest", views.latest, name="latest"),
    path("search", views.search, name="search"),
    path("<slug:slug>", views.post_page, name="post"),
]
