from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin
from .models import Announcement, Event, Text

# Register your models here.

admin.site.register(Announcement)
admin.site.register(Text)
admin.site.register(Event)
#, MarkdownModelAdmin)
