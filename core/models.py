from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from userauths.models import User
from django.utils.text import slugify
from django.utils.html import mark_safe
from taggit.managers import TaggableManager
from django.urls import reverse

# Create your models here.

STATUS = (
    ("draft", "Draft"),
    ("in_review", "In Review"),
    ("published", "Published"),
)

FEATURED = (
    ("yes", "Yes"),
    ("no", "No"),
)

def blog_images(instance, filename):
    return 'author_{0}/{1}'.format(instance.author.id, filename)

class Category(models.Model):
    title = models.CharField(max_length=60, null=True, blank=True)
    slug = models.SlugField(blank=True, null=True, unique=True, max_length=80)
    image = models.ImageField(upload_to="category", default="category.jpg")
    date = models.DateTimeField(auto_now_add=True)

    def clean_heading(self):
        self.heading = self.title.strip()  # Remove leading/trailing spaces
        return self.heading.replace(" ", "-").lower()
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.clean_heading())
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f"/blog/category/{self.slug}/"

    class Meta:
        verbose_name_plural = "Categories"

    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.title
    
class Author(models.Model):
    name = models.CharField(max_length=100, default="John Doe")
    image = models.ImageField(upload_to="author", default="author.jpg")
    description = CKEditor5Field(config_name='default', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Authors"

    def author_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.name
    
class Post(models.Model):
    heading = models.CharField(max_length=80, null=True, blank=True)
    slug = models.SlugField(blank=True, null=True, unique=True, max_length=80)
    cover = models.ImageField(upload_to=blog_images)
    body = CKEditor5Field(config_name='extends', null=True, blank=True)
    excerpt = models.CharField(max_length=450, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = TaggableManager(blank=True)
    status = models.CharField(choices=STATUS, max_length=20, default="draft")
    featured = models.CharField(choices=FEATURED, max_length=20, default="no")
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True)
    meta_title = models.CharField(max_length=60, null=True, blank=True)
    meta_description = models.CharField(max_length=160, null=True, blank=True)

    def clean_heading(self):
        self.heading = self.heading.strip()
        return self.heading.replace(" ", "-").lower()
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.clean_heading())
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('core:blog-detail', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name_plural = "Posts"

    def article_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.heading
    
class GetQuote(models.Model):
    email = models.CharField(max_length=40, default="john@email.com")

    class Meta:
        verbose_name_plural = "Quotation Requests"

    def __str__(self):
        return self.email
    
class Contact(models.Model):
    full_name = models.CharField(max_length=40, default="John Doe")
    email = models.CharField(max_length=40, default="john@email.com")
    phone = models.CharField(max_length=40, default="+1 234567890")
    subject = models.CharField(max_length=200, null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.full_name