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


class AlbumImage(models.Model):
    image = models.ImageField(upload_to='albums', blank=False)
    thumb = models.ImageField(upload_to='albums', blank=False)
    album = models.ForeignKey('album', on_delete=models.PROTECT)
    alt = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=70, editable=False)
