from django.urls import path
from . import views
app_name = 'api'
urlpatterns = [
    path('all/posts/', views.posts_list, name='all-posts'),
    path('all/contact/', views.contact_list, name='all-contact'),
    path('detail/posts/<pk>/', views.post_detail, name='detail-posts'),
    # path('one/posts/<int:pk>/', views.one_posts, name='one-posts'),
    # path('delete/posts/<int:pk>/', views.delete_post, name='delete-posts'),
]