from django.core.validators import MinValueValidator
from django.forms import IntegerField, ModelForm

from inquiries.models import Inquiry


class InquiryForm(ModelForm):
    age = IntegerField(validators=[MinValueValidator(18)])

    class Meta:
        model = Inquiry
        fields = ["name", "email", "age", "comments"]
