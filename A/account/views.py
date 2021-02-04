from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Profile
from posts.models import Post
from django.contrib.auth.decorators import login_required

def user_login(request):
    next = request.GET.get('next') 
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None :
                login(request, user)
                messages.success(request, 'You are logged in successfully', 'success')
                if next :
                    return redirect(next)
                return redirect('posts:all_posts')
            else:
                messages.error(request, 'wrong username or password !', 'warning')
    else:
        form = UserLoginForm()
    context = {'form':form}
    return render(request, 'account/login.html', context)



def user_register(request):
    if request.method =="POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
            # Way 1
            #myprofile = Profile(user = user)
            #myprofile.save()
            # -----
            login(request, user)
            messages.success(request, 'You Registered successfully', 'success')
            return redirect('posts:all_posts')
    else:
        form = UserRegistrationForm()
    context = {'form':form}
    return render(request, 'account/register.html', context)


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'You are logout in successfully', 'success')
    return redirect('posts:all_posts')


@login_required
def user_dashboard(request, user_id):
    user = get_object_or_404(User, id = user_id)
    posts = Post.objects.filter(user = user)

    self_dash = False
    if request.user.id == user_id :
        self_dash = True

    context= {
        'user': user,
        'posts': posts,
        'self_dash' : self_dash, 
    }
    return render(request, 'account/dashboard.html', context)





