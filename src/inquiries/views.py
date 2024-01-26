from django.shortcuts import render

from inquiries.forms import InquiryForm


def inquiry_form(request):
    if request.method == "POST":
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "inquiries/inquiry-success.html")
    else:
        form = InquiryForm()
    return render(request, "inquiries/inquiry-form.html", {"form": form})
