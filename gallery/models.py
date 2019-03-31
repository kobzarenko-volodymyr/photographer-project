from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1024)
    thumb = models.ImageField(upload_to='albums', blank=False)
    tags = models.CharField(max_length=250)
    is_visible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title
