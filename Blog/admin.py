from django.contrib import admin

from .models import Post, Author, Tag, Comment, Subscribers


class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date")
    list_display = ("title", "date", "author")
    populated_fields = ("slug", "title")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post")


class SubscribersAdmin(admin.ModelAdmin):
    list_display = ["Email"]


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Subscribers, SubscribersAdmin)
