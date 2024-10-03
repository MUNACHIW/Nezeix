from django.shortcuts import render, get_object_or_404
from datetime import date
from django.template.loader import render_to_string
from django.http import HttpResponseNotFound
from .models import Post
from django.views.generic import ListView


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


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "Blog/all-posts.html", {"all_posts": all_posts})


def post_detail(request, slug):
    # identified_post = next(post for post in all_posts if post["slug"] == slug)
    identified_post = get_object_or_404(Post, slug=slug)
    return render(
        request,
        "Blog/post-detail.html",
        {"post": identified_post, "post_tags": identified_post.tags.all()},
    )


def notfound(request):
    response = render_to_string("404.html")
    return HttpResponseNotFound(response)
