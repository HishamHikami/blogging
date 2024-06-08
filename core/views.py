from django.db.models import Q
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Post, Contact, GetQuote, Category, CustomTag
from django.views.generic import DetailView
import logging

# Create your views here.

def index(request):
    posts = Post.objects.filter(status="published").order_by("-date")
    f_posts = Post.objects.filter(status="published", featured="yes").order_by("-date")

    context = {
        "posts": posts,
        "f_posts": f_posts,
    }

    return render(request, 'core/index.html', context)

def blog_detail(request, category_slug, slug):
    post = get_object_or_404(Post, category__slug=category_slug, slug=slug)
    posts = Post.objects.filter(status="published").exclude(id=post.id)
    faqs = post.faqs.all()
    
    category = None
    if post.category:
        try:
            category = Category.objects.get(slug=post.category.slug)
        except Category.DoesNotExist:
            pass

    context = {
        "post": post,
        "posts": posts,
        "category": category,
        "faqs": faqs,
    }
    
    return render(request, 'core/blog-detail.html', context)

def blog_list(request):
    posts = Post.objects.filter(status="published").order_by("-date")
    f_posts = Post.objects.filter(featured="yes").order_by("-date")

    context = {
        "posts": posts,
        "f_posts": f_posts,
    }

    return render(request, 'core/blog-list.html', context)

class TagDetailView(DetailView):
    model = CustomTag
    template_name = 'core/tag.html'
    context_object_name = 'tag'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = self.get_object()
        context['posts'] = Post.objects.filter(tags=tag)
        return context

def category_list(request, category_slug=None):
    posts = Post.objects.filter(status="published").order_by("-date")

    category = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category__in=[category])

    context = {
        "posts": posts,
        "category": category,
    }

    return render(request, 'core/category.html', context)


logger = logging.getLogger(__name__)

def search_view(request):
    query = request.GET.get('q', '')
    logger.debug(f"Query: {query}")
    posts = Post.objects.filter(
        Q(heading__icontains=query) |
        Q(body__icontains=query) |
        Q(author__name__icontains=query) |
        Q(category__title__icontains=query) |
        Q(tags__name__icontains=query)
    ).distinct().order_by("-date")

    post_count = posts.count()

    context = {
        "posts": posts,
        "query": query,
        "post_count": post_count,
    }

    return render(request, 'core/search.html', context)

def ajax_contact_form(request):
    full_name = request.GET['full_name']
    email = request.GET['email']
    phone = request.GET['phone']
    subject = request.GET['subject']
    message = request.GET['message']

    contact = Contact.objects.create(
        full_name=full_name,
        email=email,
        phone=phone,
        subject=subject,
        message=message,
    )

    data = {
        "bool": True,
        "message": "Message Sent Successfully"
    }

    return JsonResponse({"data":data})

def ajax_get_quote(request):
    email = request.GET['email']

    get_quote = GetQuote.objects.create(
        email=email,
    )

    data = {
        "bool": True,
        "message": "Will get back to you soon!"
    }

    return JsonResponse({"data":data})

def robots_txt(request):
    lines = [
        "User-agent: *",
        "User-agent: Googlebot",
        "Disallow: /admin/",
        "Disallow: /nogooglebot/",
        "",
        "User-agent: *",
        "Allow: /",
        "",
        "Sitemap: https://auxnid.com/blog-sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")