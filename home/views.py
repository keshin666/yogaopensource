from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
import datetime
from home.models import Text
# Create your views here.


def index(request):
    announcements = Text.objects.filter(
        text_type='announcement',
        expiry_date__gte=datetime.date.today()
        )
    blog_entries = Text.objects.filter(
        text_type='blog_article').order_by('-created_date')
    sidebar_choices = Text.objects.filter(
        text_type='sidebar_choice', section='home').order_by('id')
    content_texts = Text.objects.filter(
        text_type='content_text', section='home')
    upcoming_days = [
        (
            (datetime.datetime.today() + datetime.timedelta(idx)).strftime(
                '%d.%m.%Y'),
            WEEKDAYS[
                (datetime.datetime.today() + datetime.timedelta(idx)).weekday()
            ]
        ) for idx in range(14)
    ]

    template = loader.get_template('home/index.html')
    context = RequestContext(request, {
        'content_texts': content_texts,
        'announcements': announcements,
        'blog_entries': blog_entries,
        'sidebar_choices': sidebar_choices,
        'upcoming_days': upcoming_days,
    })
    return HttpResponse(template.render(context))

WEEKDAYS = {
    0: 'Montag',
    1: 'Dienstag',
    2: 'Mittwoch',
    3: 'Donnerstag',
    4: 'Freitag',
    5: 'Samstag',
    6: 'Sonntag'
}
