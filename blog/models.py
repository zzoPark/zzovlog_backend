from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=128)


class Post(models.Model):
    title = models.CharField(max_length=256)
    contents = models.TextField()
    write_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name='posts')
