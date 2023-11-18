from django.contrib import admin

from posts.models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish']

    list_filter = ['pub_date', 'update_at']
    prepopulated_fields = {"slug": ['title']}

    fieldsets = [
        (
            "Post",
            {
                "fields": ['title', 'body', 'slug', 'image']
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
