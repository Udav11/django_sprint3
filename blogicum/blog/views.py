from django.shortcuts import render
from django.http import Http404
from blog.models import Post, Category
from django.db.models import Q


def index(request):
    post_list = Post.objects.select_related('category').filter(
        is_published = True,
        category__is_published = True
    )[0:5]
    context = {
        'post_list': post_list,
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    return render(request, 'blog/detail.html')


def category_posts(request, category_slug):
    post_list = Post.objects.select_related('category').filter(
        is_published = True,
        category__slug = category_slug
    )
    category = Category.objects.values().filter(
        slug=category_slug
    )

    if Category.objects.values('is_published').filter(
        slug=category_slug)[0]['is_published'] is False:
        raise Http404('Page not found')
    
    context = {
        'category': category[0],
        'post_list': post_list
    }
    return render(request, 'blog/category.html', context)

