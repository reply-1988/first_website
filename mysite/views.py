from django.shortcuts import get_object_or_404
from .models import Post, Category
from comments.forms import CommentForm
from django.views.generic import ListView, DetailView
import markdown
# Create your views here.


class CategoryView(ListView):
    model = Post
    template_name = 'mysite/detail.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        cate = get_object_or_404(Category, self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)


class PostDetailView(DetailView):
    model = Post
    template_name = 'mysite/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        response = super(PostDetailView, self).get(request, *args, **kwargs)
        self.object.increase_views()
        return response

    def get_object(self, queryset=None):
        post = super(PostDetailView, self).get_object(queryset=None)
        post.body = markdown.markdown(post.body,
                                      extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                      ])
        return post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update({
            'form': form,
            'comment_list': comment_list,
        })
        return context


class ArchivesView(ListView):
    model = Post
    template_name = 'mysite/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return super(ArchivesView, self).get_queryset().filter(created_time__year=year,
                                                               created_time__month=month).order_by('-created_time')


class IndexView(ListView):
    model = Post
    template_name = 'mysite/index.html'
    context_object_name = 'post_list'