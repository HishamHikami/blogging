"""
URL configuration for blogging project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import robots_txt
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("core.urls")),
    path('robots.txt', robots_txt),
    path("ckeditor5/", include('django_ckeditor_5.urls')),

    # Redirects (temp)
    path('/blog/category/beauty-insights/vlcc-facial-kit-for-men-top-5-alternatives-updated/', RedirectView.as_view(url='/blog/category/beauty-insights/top-5-vlcc-facial-kit-alternatives-in-2024-for-men/', permanent=True)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)