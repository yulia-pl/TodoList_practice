from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.content
