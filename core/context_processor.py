from .models import Category, Author, Post
from taggit.models import Tag

def default(request):
    categories = Category.objects.all()
    authors = Author.objects.all()
    tags = Tag.objects.all()
    latest_posts = Post.objects.filter(status="published").order_by("-date")

    return {
        'categories': categories,
        'authors': authors,
        "tags": tags,
        "latest": latest_posts,
    }