from django.contrib import admin

from posts.models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'colored_name', 'slug', 'publish']

    list_filter = ['pub_date', 'update_at']
    prepopulated_fields = {"slug": ['title']}

    fieldsets = [
        (
            "Post",
            {
                "fields": ['category', 'author', 'title', 'body', 'slug', 'image']
            }
        ),
        (
            "Options",
            {
                "classes": ['collapse'],
                "fields": ["publish", "pub_date", "update_at"]
            }
        )
    ]
