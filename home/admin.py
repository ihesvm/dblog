from django.contrib import admin

from home.models import Contact


# Register your models here.
# admin.site.register(Contact)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    list_filter = ['created_at']
    date_hierarchy = 'created_at'
