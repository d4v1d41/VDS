from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Post
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Infolink
from .models import Bigc
from .forms import CommentForm
from django.shortcuts import redirect
from .models import Post, Comment
from django.contrib.auth.decorators import login_required


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
    biggy = Bigc.objects.all()
    infos = Infolink.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[::-1]
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.html',{'post': post,'infos': infos, 'biggy': biggy})


def infol(request, info_id):
    biggy = Bigc.objects.all()
    info =get_object_or_404(Infolink, pk=info_id)
    infos = Infolink.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[::-1]
    return render(request, 'blog/infol.html',{'info': info, 'infos': infos, 'biggy':biggy})


def add_comment_to_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:detail', post_id)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


@login_required
def comment_approve(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.approve()
    return redirect('blog:detail', comment.post_id)


@login_required
def comment_remove(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('blog:detail', comment.post_id)