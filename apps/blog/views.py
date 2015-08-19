from django.shortcuts import render
from braces import views
from apps.api import models

# Create your views here.
from django.views import generic
from apps.blog import forms


class RestrictToUserMixin(object):
    def get_queryset(self):
        queryset = super(RestrictToUserMixin, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class BlogPostsListView(generic.TemplateView):
    template_name = 'blog.home.html'


class BlogPostDetailView(generic.TemplateView):
    template_name = 'post_detail.html'


class BlogPostCreateView(
    RestrictToUserMixin,
    views.LoginRequiredMixin,
    views.SetHeadlineMixin,
    generic.CreateView
):
    form_class = forms.PostForm
    headline = 'Create Blog Post'
    model = models.Post

    def __init__(self, **kwargs):
        super(BlogPostCreateView, self).__init__(**kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(BlogPostCreateView, self).form_valid(form)


