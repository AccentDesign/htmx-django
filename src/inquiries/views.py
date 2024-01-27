from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from inquiries.forms import InquiryForm


@require_http_methods(["GET", "POST"])
def inquiry_form(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "inquiries/inquiry-success.html")
    else:
        form = InquiryForm()
    return render(request, "inquiries/inquiry-form.html", {"form": form})
