from .models import Category, Author, Post, CustomTag
from django.http import HttpRequest
from django.urls import reverse, resolve, NoReverseMatch
from .models import Post, Category, CustomTag

def default(request):
    categories = Category.objects.all()[:5]
    authors = Author.objects.all()
    tags = CustomTag.objects.all()[:10]
    latest_posts = Post.objects.filter(status="published").order_by("-date")

    return {
        'categories': categories,
        'authors': authors,
        "tags": tags,
        "latest": latest_posts,
    }

STATIC_METADATA = {
    'index': {
        'title': 'Home',
        'description': 'Welcome to the homepage',
    },
    'blog': {
        'title': 'Blog',
        'description': 'Read our latest blog posts',
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
                'title': tag.name,
            }
        else:
            metadata = STATIC_METADATA.get(current_url_name, {})

    except (Post.DoesNotExist, Category.DoesNotExist, CustomTag.DoesNotExist):
        metadata = STATIC_METADATA.get(current_url_name, {})

    return {
        'meta_title': metadata.get('title', 'Default Title'),
        'meta_description': metadata.get('description', 'Default Description'),
    }

def canonical_url(request: HttpRequest) -> str:
    try:
        # Get the resolved URL name
        current_url_name = resolve(request.path_info).url_name

        # Generate the canonical URL based on the resolved URL name
        if current_url_name == 'blog-detail':
            slug = resolve(request.path_info).kwargs.get('slug')
            canonical_url = reverse('blog-detail', kwargs={'slug': slug})
        elif current_url_name == 'categories':
            category_slug = resolve(request.path_info).kwargs.get('category_slug')
            canonical_url = reverse('categories', kwargs={'category_slug': category_slug})
        elif current_url_name == 'tags':
            tag_slug = resolve(request.path_info).kwargs.get('slug')
            canonical_url = reverse('tags', kwargs={'slug': tag_slug})
        elif current_url_name in ['index', 'search', 'blog']:  # Static pages
            canonical_url = reverse(current_url_name)
        else:
            canonical_url = request.path_info  # Default to the current path as canonical
    except NoReverseMatch:
        canonical_url = request.path_info  # Fallback to the current path if reverse fails

    return {
        'canonical_url': request.build_absolute_uri(canonical_url),
    }