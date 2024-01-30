from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")


def infinite_items(request: HttpRequest, page: int) -> HttpResponse:
    def random_data(s: int, e: int):
        for i in range(s, e):
            yield {"row": i, "name": f"User {i}", "email": f"user{i}@example.com"}

    per_page = 100
    start = (page - 1) * per_page + 1
    end = start + per_page
    return render(
        request,
        "infinite/infinite-row.html",
        {"data": random_data(start, end), "next": page + 1},
    )


def tab_content(request: HttpRequest, slug: str) -> HttpResponse:
    tabs = [
        {"title": "Post Navigation", "slug": "tab1", "selected": slug == "tab1"},
        {"title": "File Uploads", "slug": "tab2", "selected": slug == "tab2"},
        {"title": "Contact Form", "slug": "tab3", "selected": slug == "tab3"},
        {"title": "Infinite Scroll", "slug": "tab4", "selected": slug == "tab4"},
    ]
    return render(request, f"tabs/{slug}.html", {"tabs": tabs})
