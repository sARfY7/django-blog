from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Post, Tag
from .forms import PostForm
import json

# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False)
    return render(request, 'blog/post_list.html', {'posts': posts, 'drafts': False})


def post_detail(request, id):
    post = Post.objects.get(pk=id)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post_title = form.cleaned_data['title']
            post_text = form.cleaned_data['text']
            post_tags = [Tag.objects.create(name=tag) for tag in form.cleaned_data['tags'].split(',')]
            post = Post.objects.create(title=post_title, text=post_text, author=request.user)
            post.tags.set(post_tags)
            return redirect('post_detail', id=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form, 'author': request.user, 'edit': False})

@login_required
def post_edit(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            updated_post_title = form.cleaned_data['title']
            updated_post_text = form.cleaned_data['text']
            updated_post_tags = form.cleaned_data['tags'].split(',')
            tags_not_to_delete = []
            post_tags = post.tags.all()
            post_tag_names = [tag.name for tag in post_tags]
            for tag in updated_post_tags:
                if tag not in post_tag_names:
                    post.tags.create(name=tag)
            for tag in post_tags:
                if tag.name not in updated_post_tags:
                    post.tags.remove(tag)
            updated_post = Post.objects.filter(id=id).update(title=updated_post_title, text=updated_post_text)            
            return redirect('post_detail', id=id)
    else:
        post_tags = ''
        post_tags = ','.join([tag.name for tag in post.tags.all()])
        form = PostForm({'title': post.title, 'text': post.text, 'tags': post_tags})
    return render(request, 'blog/post_edit.html', {'form': form, 'author': post.author, 'edit': True})

@login_required
def post_delete(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect('post_list')

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True)
    return render(request, 'blog/post_list.html', {'posts': posts, 'drafts': True})

@login_required
def post_draft_publish(request, id):
    post = get_object_or_404(Post, pk=id)
    post.publish()
    return redirect('post_detail', id=post.pk)


def tag_post_list(request, tag_name):
    posts = Post.objects.filter(tags__name=tag_name)
    return render(request, 'blog/post_list.html', {'posts': posts, 'drafts': False})