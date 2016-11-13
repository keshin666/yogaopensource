from django.db import models
from django.contrib.auth.models import User
from django_markdown.models import MarkdownField
import markdown

# Create your models here.


class Announcement(models.Model):
    text = models.TextField()
    date = models.DateTimeField()
    expiry_date = models.DateTimeField()
    author = models.ForeignKey(User)

    def __str__(self):
        return self.text


class Event(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    description = models.TextField(default=None, blank=True, null=True)
    event_date = models.DateTimeField()
    venue = models.CharField(max_length=255,
                             default=None,
                             blank=True,
                             null=True)
    author = models.ForeignKey(User)
    additional_data = models.TextField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name + ' ' + self.event_date.strftime("%Y-%m-%d")


class Text(models.Model):
    text_type = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255,
                                default=None,
                                blank=True,
                                null=True)
    section = models.CharField(max_length=255,
                               default=None,
                               blank=True,
                               null=True)
    anchor = models.CharField(max_length=255,
                              default=None,
                              blank=True,
                              null=True)
    text = MarkdownField()
    created_date = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField(default=None, blank=True, null=True)
    author = models.ForeignKey(User)
    additional_data = models.TextField(default=None, blank=True, null=True)

    def __str__(self):
        return (self.text_type
                + ': '
                + self.title)

    def get_title_preview(self):
        title = self.title
        return title if len(title) < 58 else (title[:58] + '...')

    def get_text_preview(self):
        text = self.text
        return text if len(text) <= 160 else (text[:160] + '...')

    def get_text_preview_md(self):
        text = self.text
        return (markdown.markdown(text, safe_mode=True) if len(text) <= 160
                else markdown.markdown(text[:160] + '...', safe_mode=True))

    def render_text_markdown(self):
        return markdown.markdown(
            self.text,
            safe_mode=True,
            extensions=['markdown.extensions.nl2br',
                        'markdown.extensions.tables',
                        'markdown.extensions.sane_lists',
                        'markdown.extensions.attr_list',
                        'markdown.extensions.def_list',
                        'markdown.extensions.footnotes'])
