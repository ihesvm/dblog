from django.urls import path


from . import views


app_name = 'category'
urlpatterns = [
    path('related/<name>', views.related_post, name="related-posts")
]