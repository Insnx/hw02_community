from django.shortcuts import render, get_object_or_404

from .models import Post, Group

COUNT_POSTS = 10
# Самая главная страница
def index(request):
    posts = Post.objects.all()[:COUNT_POSTS]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


# Страница со списком мороженого
def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:COUNT_POSTS]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
