from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Post, Category
from taggit.models import Tag

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = "weekly"

    def items(self):
        return [""] # Add static page names here

    def location(self, item):
        return reverse(item)
    
class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Post.objects.filter(status="published")
    
    def lastmod(self, obj):
        return obj.updated
    
class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Category.objects.all()
    
    def lastmod(self, obj):
        return obj.date
    
class TagSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Tag.objects.all()
    
    def lastmod(self, obj):
        tagged_posts = Post.objects.filter(tags=obj)
        if tagged_posts.exists():
            return tagged_posts.latest('date').date
        return None