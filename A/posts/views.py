from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import AddPostForm
from django.contrib import messages
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required


def all_posts(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request,'posts/all_posts.html' , context)


def post_detail(request, year, month, day, slug):
    print(year, month, day, slug)
    post = get_object_or_404(Post, created__year = year, created__month = month, created__day = day, slug=slug)
    context = {'post':post}
    return render(request, 'posts/post_detail.html', context)


@login_required
def add_post(request, user_id):
    if request.user.id == user_id:
        if request.method == 'POST':
            form = AddPostForm(request.POST)
            if form.is_valid():
                new_post = form.save(commit=False)
                new_post.user = request.user
                new_post.slug = slugify(form.cleaned_data['body'][:30])
                new_post.save()
                messages.success(request, 'your post submitted', 'success')
                return redirect('account:dashboard', user_id)
        else:
            form = AddPostForm()
        context = {'form': form}
        return render(request, 'posts/add_posts.html', context)
    else:
        return redirect('posts:all_posts')


@login_required
def post_delete(request, user_id, post_id):
    if user_id == request.user.id:
        p = Post.objects.filter(id = post_id)
        p.delete()
        messages.success(request, 'your post deleted successfully', 'success')
        return redirect('account:dashboard', user_id)
    else:
        return redirect('posts:all_posts')