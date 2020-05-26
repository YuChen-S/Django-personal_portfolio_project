from django.shortcuts import render, get_object_or_404
from .models import blog_projects
# Create your views here.
def all_blogs(request):
    projects = blog_projects.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html', {'projects':projects})

def detail(request, blog_id):
    blog = get_object_or_404(blog_projects, pk = blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})
