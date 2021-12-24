from django.shortcuts import redirect, render, get_object_or_404, reverse 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Comment, Category
from django.contrib.auth.models import User
from .forms import CommentForm
from datetime import datetime
from users.models import Profile

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5
    
    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context  
    
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_profile_post.html'
    context_object_name = 'posts'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted') 
               
    def get_context_data(self, **kwargs):
        context = super(UserPostListView, self).get_context_data(**kwargs)
        context['profiles'] = Profile.objects.filter(user__username=self.kwargs.get('username'))
        context['num_post'] = Post.objects.filter(author__username=self.kwargs.get('username')).count
        return context   
class CategoryListView(ListView):
    model = Post
    template_name = 'blog/category_post.html'
    context_object_name = 'posts'

    def get_queryset(self):
        tag = get_object_or_404(Category, name=self.kwargs.get('name'))
        return Post.objects.filter(category=tag).order_by('-date_posted') 
    
    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['tag'] = self.kwargs.get('name')
        return context   
    
    
class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['num_comment'] = Comment.objects.filter(post=self.kwargs.get('pk')).count
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'teaser', 'content', 'category']
    success_url = '/'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'teaser', 'content', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
    def get_success_url(self):
           pk = self.kwargs["pk"]
           return reverse("post-detail", kwargs={"pk": pk})

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

 
def add_comment(request, pk):    
    eachPost = get_object_or_404(Post,id=pk)
    form = CommentForm(instance=eachPost)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=eachPost)
        if form.is_valid():
            name = request.user.username
            body_comment = form.cleaned_data['body']
            c = Comment(post=eachPost, author=User.objects.get(username=name), 
                       body=body_comment, date_posted=datetime.now())            
            c.save()
            return redirect(reverse('post-detail', args=[eachPost.id]))
        else:
            print('form is invalid')    
    else:
        form = CommentForm()    


    context = {
        'form': form
    }

    return render(request, 'blog/add_comment.html', context)
