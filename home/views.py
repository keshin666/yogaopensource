from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from home.models import Announcement
from blog.models import BlogEntry
# Create your views here.


def index(request):
    announcements = Announcement.objects.order_by('-date')
    blog_entries = BlogEntry.objects.order_by('-date')
    template = loader.get_template('home/index.html')
    context = RequestContext(request, {
        'announcements': announcements,
        'blog_entries': blog_entries,
    })
    return HttpResponse(template.render(context))
