from django.contrib import admin
from core.models import Post, Author, Category, GetQuote
from taggit.models import Tag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['heading', 'slug', 'status', 'category', 'author']
    readonly_fields = ['slug']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    readonly_fields = ['slug']

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'user']

class GetQuoteAdmin(admin.ModelAdmin):
    list_display = ['email']
    readonly_fields = ['email']

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(GetQuote, GetQuoteAdmin)
admin.site.unregister(Tag)