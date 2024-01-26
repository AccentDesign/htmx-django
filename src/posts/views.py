from django.shortcuts import get_object_or_404, render

from posts.models import Post


def post_page(request, slug: str):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "posts/post.html", {"post": post})


def latest(request):
    posts = Post.objects.get_latest(5)
    return render(request, "posts/latest-results.html", {"posts": posts})


def search(request):
    s = request.GET.get("search", "").strip()
    posts = Post.objects.search(s)
    return render(request, "posts/search-results.html", {"posts": posts})
