from django.shortcuts import render, get_object_or_404
from datetime import date
from django.template.loader import render_to_string
from django.http import HttpResponseNotFound, HttpResponseRedirect
from .models import Post
from django.views.generic import ListView, DetailView
from .forms import CommentForm
from django.views import View
from django.urls import reverse


# Create your views here.
class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    # changing context objectname for it to be used
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


class AllPostView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"


# def posts(request):
#     all_posts = Post.objects.all().order_by("-date")
#     return render(request, "Blog/all-posts.html", {"all_posts": all_posts})


class SinglePostView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
        }
        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
        }
        return render(request, "blog/post-detail.html", context)

    # for getting correct slug if you are not using id or primary key or detail to also get or access tags


# def post_detail(request, slug):
#     # identified_post = next(post for post in all_posts if post["slug"] == slug)
#     identified_post = get_object_or_404(Post, slug=slug)
#     return render(
#         request,
#         "Blog/post-detail.html",
#         {"post": identified_post, "post_tags": identified_post.tags.all()},
#     )


def notfound(request):
    response = render_to_string("404.html")
    return HttpResponseNotFound(response)
