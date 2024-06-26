from django.urls import path
from .views import blog_detail, blog_list, index, ajax_contact_form, ajax_get_quote, category_list, search_view, TagDetailView
from django.contrib.sitemaps.views import sitemap
from .sitemap import BlogSitemap, CategorySitemap, TagSitemap

app_name = "core"

sitemaps = {
    'posts': BlogSitemap,
    'categories': CategorySitemap,
    'tags': TagSitemap,
}

urlpatterns = [
    path("", index, name='index'),
    path("blog/", blog_list, name='blog'),
    path("blog/category/<str:category_slug>/", category_list, name='categories'),
    path("blog/category/<str:category_slug>/<str:slug>/", blog_detail, name='blog-detail'),
    path("blog/tag/<slug:slug>/", TagDetailView.as_view(), name='tags'),
    path("search/", search_view, name="search"),
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