from django.shortcuts import render, get_object_or_404

from category.models import Category


# Create your views here.


def related_post(request, name):
    cat = get_object_or_404(Category, name=name)
    cat_name = cat.name

    posts = cat.posts.filter(publish='p')

    return render(request, 'category/related.html', {'posts': posts, 'name': cat_name})
