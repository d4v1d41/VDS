from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Post
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Infolink
from .models import Bigc
def index(request):
    biggy = Bigc.objects.all()
    infos = Infolink.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[::-1]
    posts_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[::-1]
    page = request.GET.get('page', 1)
    paginator = Paginator(posts_list, 6)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/index.html', {'posts': posts, 'infos': infos, 'biggy': biggy})
    # POSTS


def detail(request, post_id):
    infos = Infolink.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[::-1]
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.html',{'post': post,'infos':infos})

def infol(request, info_id):
    info =get_object_or_404(Infolink, pk=info_id)
    infos = Infolink.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[::-1]
    return render(request, 'blog/infol.html',{'info': info, 'infos': infos})