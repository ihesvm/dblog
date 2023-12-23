from django.urls import path
from . import views
app_name = 'api'
urlpatterns = [
    path('all/posts/', views.all_posts, name='all-posts'),
    # path('one/posts/<int:pk>/', views.one_posts, name='one-posts'),
    # path('delete/posts/<int:pk>/', views.delete_post, name='delete-posts'),
]