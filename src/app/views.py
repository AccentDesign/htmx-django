from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def tab_content(request, slug: str):
    tabs = [
        {"title": "Post Navigation", "slug": "tab1", "selected": slug == "tab1"},
        {"title": "File Uploads", "slug": "tab2", "selected": slug == "tab2"},
        {"title": "Contact Form", "slug": "tab3", "selected": slug == "tab3"},
    ]
    return render(request, f"tabs/{slug}.html", {"tabs": tabs})
