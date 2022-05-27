from datetime import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from blog.forms import PostForm, AuthUserForm, ReigsterUserForm
from blog.models import Post
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import User
from django.contrib.auth import login, authenticate


# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/post_list.html', {"items": posts})


class Postlist(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'items'


class PostCreateView(CreateView):
    form_class = PostForm
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy('post_list')


def post_detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_edit(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'GET':
        form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})
    else:
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_date = datetime.now()
            post.published_date = datetime.now()
            post.save()
            return redirect('post_detail', post_pk=post.pk)


def post_delete(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk).delete()
    return redirect('post_list')


class MyProjectLoginView(LoginView):
    template_name = 'blog/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('post_list')

    def get_success_url(self):
        return self.success_url


class RegisterUserView(CreateView):
    model = User
    form_class = ReigsterUserForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        auth_user = authenticate(username=username, password=password)
        login(self.request, auth_user)
        return form_valid



class MyProjectLogoutView(LogoutView):
    next_page = reverse_lazy('post_list')
