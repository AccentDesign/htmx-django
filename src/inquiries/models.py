from django.db import models


class InquiryManager(models.Manager):
    pass


class Inquiry(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    age = models.IntegerField()
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    objects = InquiryManager()

    class Meta:
        verbose_name_plural = "Inquiries"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
