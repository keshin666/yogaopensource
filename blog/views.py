from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from blog.models import BlogEntry

# Create your views here.


def index(request):
    blog_entries = BlogEntry.objects.order_by('-date')
    template = loader.get_template('blog/index.html')
    context = RequestContext(request, {
        'blog_entries': blog_entries,
    })
    return HttpResponse(template.render(context))


def view_blog_entry(request, blog_entry_id):
    blog_entry = get_object_or_404(BlogEntry, pk=blog_entry_id)
    template = loader.get_template('blog/blog_entry.html')
    context = RequestContext(request, {
        'blog_entry': blog_entry,
        })
    return HttpResponse(template.render(context))
