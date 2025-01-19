from django.shortcuts import render
from django.http import Http404

posts = []

post_for_id = {post['id']: post for post in posts}


def index(request):
    return render(request, 'blog/index.html', {'post': reversed(posts)})


def post_detail(request, post_id):
    try:
        context = {'post': post_for_id[post_id]}
    except Exception:
        raise Http404()
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    return render(request, 'blog/category.html',
                  {'category_slug': category_slug})
