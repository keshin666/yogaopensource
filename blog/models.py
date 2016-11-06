from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# class BlogEntry(models.Model):
#     title = models.CharField(max_length=350)
#     text = models.TextField()
#     date = models.DateTimeField()
#     author = models.ForeignKey(User)

#     def __str__(self):
#         return self.title

#     def get_title_preview(self):
#         title = self.title
#         return title if len(title) < 58 else (title[:58] + '...')

#     def get_text_preview(self):
#         text = self.text
#         return text if len(text) <= 255 else (text[:255] + '...')