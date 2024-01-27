from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_GET

from posts.models import Post


@require_GET
def post_page(request: HttpRequest, slug: str) -> HttpResponse:
    post = get_object_or_404(Post, slug=slug)
    return render(request, "posts/post.html", {"post": post})


@require_GET
def latest(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.get_latest(5)
    return render(request, "posts/latest-results.html", {"posts": posts})


@require_GET
def search(request: HttpRequest) -> HttpResponse:
    s = request.GET.get("search", "").strip()
    posts = Post.objects.search(s)
    return render(request, "posts/search-results.html", {"posts": posts})
