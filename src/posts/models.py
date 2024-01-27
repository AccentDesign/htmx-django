from django.db import models
from django.db.models import Q, QuerySet


class PostManager(models.Manager):
    def get_latest(self, number: int) -> QuerySet:
        return self.order_by("-created_at")[:number]

    def search(self, query: str) -> QuerySet:
        if not query.strip():
            return self.none()
        filters = [Q(title__icontains=t) for t in query.strip().split(" ")]
        return self.filter(*filters)


class Post(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = PostManager()

    class Meta:
        ordering = ["slug"]

    def __str__(self):
        return self.slug
