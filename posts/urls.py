from django.urls import path


from posts import views


app_name = 'posts'
urlpatterns = [
    path('get/<slug:slug>/', views.PostDetail.as_view(), name='posts-get'),
    path('forms/', views.PostView.as_view(), name="posts-form"),
]