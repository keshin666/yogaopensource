from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render

# Create your views here.


def index(request):
    template = loader.get_template('ashtangayoga/index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))
