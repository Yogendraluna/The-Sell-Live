from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
)
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from olx.models import Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ('product_name', 'product_description','price', 'image', 'phone_number',)
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'home.html'
    login_url = 'login'

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'
    login_url = 'login'

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ('product_name', 'product_description','price', 'image', 'phone_number',)
    template_name = 'post_edit.html'
    login_url = 'login'

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
    login_url = 'login'
