from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from home.models import Text

# Create your views here.


def index(request):
    template = loader.get_template('ashtangayoga/index.html')
    sidebar_choices = Text.objects.filter(
        text_type='sidebar_choice', section='ashtangayoga')
    content_texts = Text.objects.filter(
        text_type='content_text', section='ashtangayoga')
    context = RequestContext(request, {
        'sidebar_choices': sidebar_choices,
        'content_texts': content_texts,
        })
    return HttpResponse(template.render(context))