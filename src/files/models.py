from os.path import basename

from django.db import models


class FileManager(models.Manager):
    pass


class File(models.Model):
    file = models.FileField(upload_to="uploads/")
    file_name = models.CharField(max_length=255, editable=False)
    size = models.PositiveIntegerField(editable=False)
    content_type = models.CharField(max_length=100, editable=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    objects = FileManager()

    class Meta:
        ordering = ["file_name"]

    def save(self, *args, **kwargs):
        self.size = self.file.size
        self.file_name = basename(self.file.name)
        self.content_type = self.file.file.content_type
        super().save(*args, **kwargs)

    def __str__(self):
        return self.file_name
