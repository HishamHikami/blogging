from .models import Category, Author, Post, CustomTag

def default(request):
    categories = Category.objects.all()
    authors = Author.objects.all()
    tags = CustomTag.objects.all()
    latest_posts = Post.objects.filter(status="published").order_by("-date")

    return {
        'categories': categories,
        'authors': authors,
        "tags": tags,
        "latest": latest_posts,
    }