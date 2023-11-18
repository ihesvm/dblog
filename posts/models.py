from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.datetime_safe import datetime
from django.utils.text import slugify


# class PostManager(models.Manager):
#     def just_published(self):
#         return self.filter(publish=True)

#     def slugs(self, slug):
#         return self.get(slug=slug)


class PostManager(models.Manager):
    def published(self):
        return self.filter(publish=True).order_by('-pub_date')


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=1000)
    slug = models.SlugField(null=True, blank=True)
    publish = models.BooleanField(default=False)
    image = models.ImageField(upload_to='posts/image/', max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True, blank=True)
    pub_date = models.DateTimeField(null=True, blank=True)

    posts = PostManager()
    objects = models.Manager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)

        if self.publish:
            self.pub_date = datetime.now()
        return super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:posts-get', args=[str(self.slug)])

    class Meta:
        indexes = [models.Index(fields=('title', 'slug'))]
        verbose_name = 'Post'
        verbose_name_plural = 'Post'
