from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = 'home'
urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('about/', TemplateView.as_view(template_name='home/index.html'), name="about"),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('register/', views.SignupView.as_view(), name="register"),
    path('logout/', views.user_logout, name="logout"),
    path('profile/', views.ProfileView.as_view(), name="profile"),
    # path('save/contact/', views.save_contact, name="save-contact"),
]