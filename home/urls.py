from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = 'home'
urlpatterns = [
    path('', TemplateView.as_view(template_name='home/index.html'), name="home"),
    path('about/', TemplateView.as_view(template_name='home/index.html'), name="about"),
    path('contact/', views.ContactView.as_view(), name="contact"),
    # path('save/contact/', views.save_contact, name="save-contact"),
]