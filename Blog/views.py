from django.shortcuts import render
from datetime import date
from django.template.loader import render_to_string
from django.http import HttpResponseNotFound
from .models import Post

all_posts = []


def get_date(post):
    return post["date"]


# Create your views here.
def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:1]
    return render(request, "Blog/index.html", {"posts": latest_posts})


def posts(request):
    return render(request, "Blog/all-posts.html", {"all_posts": all_posts})


def post_detail(request, slug):
    try:
        identified_post = next(post for post in all_posts if post["slug"] == slug)
        return render(request, "Blog/post-detail.html", {"post": identified_post})
    except:
        response = render_to_string("404.html")
        return HttpResponseNotFound(response)


def notfound(request):
    response = render_to_string("404.html")
    return HttpResponseNotFound(response)
