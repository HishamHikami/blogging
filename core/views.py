from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Post, Contact, GetQuote
from taggit.models import Tag

# Create your views here.

def index(request):
    posts = Post.objects.filter(status="published").order_by("-date")
    f_posts = Post.objects.filter(featured="yes").order_by("-date")

    context = {
        "posts": posts,
        "f_posts": f_posts,
    }

    return render(request, 'core/index.html', context)

def blog_detail(request, slug):
    post = Post.objects.get(slug=slug)
    posts = Post.objects.filter(status="published")

    context = {
        "post": post,
        "posts": posts,
    }
    
    return render(request, 'blog/blog-detail.html', context)

def blog_list(request):
    posts = Post.objects.filter(status="published").order_by("-date")
    f_posts = Post.objects.filter(featured="yes").order_by("-date")

    context = {
        "posts": posts,
        "f_posts": f_posts,
    }

    return render(request, 'blog/blog-list.html', context)

def tag_list(request, tag_slug=None):
    posts = Post.objects.filter(status="published").order_by("-date")

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    context = {
        "posts": posts,
        "tag": tag,
    }

    return render(request, 'blog/tag.html', context)

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