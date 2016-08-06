from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BlogEntry(models.Model):
    title = models.CharField(max_length=350)
    text = models.TextField()
    date = models.DateTimeField()
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title
