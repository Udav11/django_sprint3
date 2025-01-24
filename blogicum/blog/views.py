from django.shortcuts import render, get_object_or_404
from django.http import Http404
from blog.models import Post, Category
from django.db.models.functions import Now


def index(request):
    post_list = Post.objects.select_related('author', 'category',
                                            'location').filter(
        is_published=True,
        category__is_published=True,
        pub_date__lt=Now(),
    )[0:5]
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, post_id):
    post_list = get_object_or_404(
        Post.objects.select_related(
            'author', 'category', 'location',
        ).filter(pub_date__lt=Now(),
                 is_published=True,
                 category__is_published=True
                 ), id=post_id
    )
    return render(request, 'blog/detail.html', {'post': post_list})


def category_posts(request, category_slug):
    post_list = Post.objects.select_related('category').filter(
        is_published=True,
        category__slug=category_slug,
        pub_date__lt=Now()
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
