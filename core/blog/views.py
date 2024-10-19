from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.
def blogPage(request):
    post = blogModel.objects.all()
    
    context = {
        'post':post,
    }
    return render(request, 'blog.html', context)
def singelPage(request, slug):
    singel = get_object_or_404(blogModel, slug = slug)
    blg_cat = blogCatagory.objects.all()
    recent_posts = blogModel.objects.order_by('post_date')[:5]
    context = {
        'singel':singel,
        'blg_cat':blg_cat,
        'recent_posts':recent_posts,
    }
    return render(request, 'single.html', context)
