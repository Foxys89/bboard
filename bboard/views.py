from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView,\
    UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Reply
from .forms import PostForm
from .filters import PostFilter


class PostsList(ListView):
    model = Post
    ordering = '-time'
    template_name = 'postslist.html'
    context_object_name = 'posts'
    paginate_by = 50

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostCreate(CreateView):
    permission_required = ('news.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        return super().form_valid(form)


class PostEdit(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts_list')