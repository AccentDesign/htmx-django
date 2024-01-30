from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("files/", include("files.urls", namespace="files")),
    path("inquiries/", include("inquiries.urls", namespace="inquiries")),
    path("posts/", include("posts.urls", namespace="posts")),
    path("infinite/<int:page>", views.infinite_items, name="infinite-items"),
    path("tabs/<slug:slug>", views.tab_content, name="tabs"),
    path("", views.index, name="index"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
