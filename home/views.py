from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from home.models import Announcement
# Create your views here.


def index(request):
    announcements = Announcement.objects.order_by('-date')
    template = loader.get_template('home/index.html')
    context = RequestContext(request, {
        'announcements': announcements,
    })
    return HttpResponse(template.render(context))
