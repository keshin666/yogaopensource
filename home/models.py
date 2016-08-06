from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Announcement(models.Model):
    text = models.TextField()
    date = models.DateTimeField()
    expiry_date = models.DateTimeField()
    author = models.ForeignKey(User)

    def __str__(self):
        return self.text
