from django.urls import path
from . import views
app_name = 'api'
urlpatterns = [
    # path('all/posts/', views.posts_list, name='all-posts'),
    # path('contact/<int:pk>/', views.ContactView.as_view(), name='all-contact'),
    path('contact/', views.ContactApiView.as_view(), name='all-contact'),
    path('posts/', views.PostApiView.as_view(), name='all-posts'),
    path('posts/<int:pk>/', views.PostApiDetail.as_view(), name='all-posts'),
    # path('detail/posts/<pk>/', views.post_detail, name='detail-posts'),

    # path('one/posts/<int:pk>/', views.one_posts, name='one-posts'),
    # path('delete/posts/<int:pk>/', views.delete_post, name='delete-posts'),
]