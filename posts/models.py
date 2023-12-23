import uuid

from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.datetime_safe import datetime
from django.utils.html import format_html
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.search import SearchVector
from category.models import Category
from django.db.models.functions import Concat

# class PostManager(models.Manager):
#     def just_published(self):
#         return self.filter(publish=True)

#     def slugs(self, slug):
#         return self.get(slug=slug)


class PostManager(models.Manager):
    def published(self):
        return self.filter(publish='p').order_by('-pub_date')
    

    def search_by_title(self, value):
        return self.annotate(
            search=SearchVector('title')
        ).filter(search__icontains=value)



class PostQuerySet(models.QuerySet):
    def get_author_title(self):
        return self.annotate(
            at=Concat("title", models.Value(" "), "author__username")
        )
    


    def get_unique_title(self):
        return self.aggregate(
            titles=models.Count("title", distinct=True)
        )
    


    def get_id(self, id):
        return self.get(id=id)



# Create your models here.
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'd', _('Draft')
        PUBLISH = 'p', _('Publish')

        __empty__ = _('Empty')

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ManyToManyField(Category, null=True, blank=True, related_name="posts")
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=1000)
    slug = models.SlugField(null=True, blank=True, unique=True)
    # publish = models.BooleanField(default=False)
    publish = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    image = models.ImageField(upload_to='posts/image/', max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True, blank=True)
    pub_date = models.DateTimeField(null=True, blank=True)
    uniqueId = models.CharField(max_length=255, null=True, blank=True)
    views = models.PositiveIntegerField(default=0)

    posts = PostManager()
    objects = PostQuerySet().as_manager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        if self.uniqueId is None:
            self.uniqueId = str(uuid.uuid4()).split('-')[4]
            self.slug = slugify('{}{}'.format(self.title, self.uniqueId))

        self.slug = slugify('{}{}'.format(self.title, self.uniqueId))

        if self.publish == self.Status.PUBLISH:
            self.pub_date = datetime.now()
        return super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:posts-get', args=[str(self.slug)])

    @admin.display(description='title')
    def colored_name(self):
        return format_html(
            '<span style="color: green;">{}</span>',
            self.title
        )

    @property
    def get_author_name(self):
        return self.author.username

    class Meta:
        indexes = [models.Index(fields=('title', 'slug'))]
        verbose_name = 'Post'
        verbose_name_plural = 'Post'
