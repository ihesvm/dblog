from django.urls import path

from posts.views import all_posts, get_posts, post_form, post_save
from posts import views
urlpatterns = [
    path('', views.PostListView.as_view(), name='posts-all'),
    path('get/<slug:slug>/', views.PostDetail.as_view(), name='posts-get'),
    path('forms/', post_form, name="posts-form"),
    path('save/', post_save, name="posts-save")
]