from django.urls import path


from posts import views


app_name = 'posts'
urlpatterns = [
    path('get/<slug:slug>/', views.PostDetail.as_view(), name='posts-get'),
    path('forms/', views.PostCreateView.as_view(), name="posts-form"),
    path('delete/<slug>/', views.PostDeleteView.as_view(), name="posts-delete"),
    path('update/<slug>/', views.PostUpdateView.as_view(), name="posts-update"),
]