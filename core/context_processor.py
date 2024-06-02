from .models import Category, Author, Post, CustomTag
from django.urls import reverse, resolve, NoReverseMatch
from .models import Post, Category, CustomTag

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

STATIC_METADATA = {
    'index': {
        'title': 'Holistic Health & Beauty Blog | Natural Well-Being Tips & Inspiration',
        'description': 'Discover expert tips and inspiration for holistic health, natural beauty, and overall well-being. Embrace a balanced lifestyle with our guides on fitness, skincare, nutrition, and more.',
    },
    'blog': {
        'title': 'Health, Beauty & Wellness Blog | Expert Tips & Natural Insights',
        'description': 'Explore our blog for the latest articles on holistic health, natural beauty, and overall wellness. Find expert advice, DIY tips, and inspiration to enhance your well-being naturally.',
    },
    'search': {
        'title': 'Search Results',
        'description': 'Search through our articles',
    },
}

def metadata(request):
    try:
        current_url_name = resolve(request.path_info).url_name
        metadata = None

        if current_url_name == 'blog-detail':
            slug = resolve(request.path_info).kwargs.get('slug')
            post = Post.objects.get(slug=slug)
            metadata = {
                'title': post.meta_title,
                'description': post.meta_description,
            }
        elif current_url_name == 'categories':
            category_slug = resolve(request.path_info).kwargs.get('category_slug')
            category = Category.objects.get(slug=category_slug)
            metadata = {
                'title': category.meta_title,
                'description': category.meta_description,
            }
        elif current_url_name == 'tags':
            tag_slug = resolve(request.path_info).kwargs.get('slug')
            tag = CustomTag.objects.get(slug=tag_slug)
            metadata = {
                'title': tag.meta_title,
                'description': tag.meta_description,
            }
        else:
            metadata = STATIC_METADATA.get(current_url_name, {})

        canonical_url = request.build_absolute_uri(reverse(current_url_name, kwargs=resolve(request.path_info).kwargs))

    except (Post.DoesNotExist, Category.DoesNotExist, CustomTag.DoesNotExist, NoReverseMatch):
        metadata = STATIC_METADATA.get(current_url_name, {})
        canonical_url = request.build_absolute_uri(request.path_info)

    return {
        'meta_title': metadata.get('title', 'Default Title'),
        'meta_description': metadata.get('description', 'Default Description'),
        'canonical_url': canonical_url,
    }