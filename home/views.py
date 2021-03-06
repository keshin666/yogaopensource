from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from datetime import date, timedelta
from home.models import Text, Event
# Create your views here.


def index(request):
    announcements = Text.objects.filter(text_type='announcement').exclude(
        Q(expiry_date__lt=date.today()) & Q(expiry_date__isnull=False)
    )
    blog_entries = Text.objects.filter(text_type='blog_article',).exclude(
        Q(expiry_date__lt=date.today()) & Q(expiry_date__isnull=False)
    ).order_by('-created_date')
    sidebar_choices = Text.objects.filter(
        text_type='sidebar_choice',
        section='home').exclude(
        Q(expiry_date__lt=date.today()) & Q(expiry_date__isnull=False)
    ).order_by('id')
    content_texts = Text.objects.filter(
        text_type='content_text',
        section='home').exclude(
        Q(expiry_date__lt=date.today()) & Q(expiry_date__isnull=False)
    )
    upcoming_days = [
        {
            'date': (date.today() + timedelta(idx)).strftime('%d.%m.%Y'),
            'weekday': WEEKDAYS[(date.today() + timedelta(idx)).weekday()],
            'events': Event.objects.filter(
                event_date__date=date.today() + timedelta(idx))
        } for idx in range(14)
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
