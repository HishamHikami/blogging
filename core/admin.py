from django.contrib import admin
from core.models import Post, Author, Category, GetQuote, FAQ, CustomTag
from taggit.models import Tag

# Register your models here.

class FAQInline(admin.StackedInline):  # or admin.TabularInline
    model = FAQ
    extra = 1  # Number of empty forms to display

class PostAdmin(admin.ModelAdmin):
    list_display = ['heading', 'slug', 'status', 'category', 'author']
    readonly_fields = ['slug']
    inlines = [FAQInline]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    readonly_fields = ['slug']

class CustomTagAdmin(admin.ModelAdmin):
    list_display = ['name', 'meta_title']
    readonly_fields = ['name', 'slug']

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'user']

class GetQuoteAdmin(admin.ModelAdmin):
    list_display = ['email']
    readonly_fields = ['email']

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(GetQuote, GetQuoteAdmin)
admin.site.register(CustomTag, CustomTagAdmin)
admin.site.unregister(Tag)