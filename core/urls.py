from django.urls import path
from .views import blog_detail, blog_list, tag_list, index, ajax_contact_form, ajax_get_quote
from django.contrib.sitemaps.views import sitemap
from .sitemap import BlogSitemap

app_name = "blog"

sitemaps = {
    'posts': BlogSitemap
}

urlpatterns = [
    path("", index, name='index'),
    path("blog/", blog_list, name='blog'),
    path("blog/<slug>", blog_detail, name='blog-detail'),
    path("blog/tag/<tag_slug>/", tag_list, name='tags'),
    path(
        "blog-sitemap.xml",
        sitemap,
        {
            'sitemaps': sitemaps
        },
        name = 'django.contrib.sitemaps.views.sitemap'
    ),
    path("ajax-contact-form/", ajax_contact_form, name="ajax-contact-form"),
    path("ajax-get-quote/", ajax_get_quote, name="ajax-get-quote"),
]