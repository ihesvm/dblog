from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse

from home.forms import ContactForm, SignupForm, LoginForm
from django.views.generic import CreateView, View, ListView
from django.views.generic.edit import FormMixin

from posts.models import Post


# Create your views here.

# def index(request):
#     return render(request, 'home/index.html', {})


# def about(request):
#     return render(request, 'home/about.html', {})


# class ContactFormView(CreateView):
#     template_name = 'home/contact.html'
#     form_class = ContactForm

# def contact(request):
#     form = ContactForm()
#     return render(request, 'home/contact.html', {'form': form})


# def save_contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')

#     return redirect('contact')


class PostListView(ListView):
    model = Post
    queryset = Post.posts.published()
    template_name = 'posts/all_posts.html'


class ContactView(View):
    # form_class = ContactForm

    __form = ContactForm

    def get(self, request, *args, **kwargs):
        return render(request, 'home/contact.html', {'form': self.__form()})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = self.__form(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Contact Created !!!')
                return redirect('home:home')

        messages.warning(request, 'Contact Error !!!')
        return redirect('home:contact')


class SignupView(View):
    __form = SignupForm

    def get(self, request):
        return render(request, 'authenticate/register.html', {'form': self.__form()})

    def post(self, request):
        if request.method == 'POST':
            form = self.__form(request.POST)

            if form.is_valid():
                form.save()
                messages.success(request, 'User Created !!!')

                return redirect('home:login')

        messages.warning(request, 'User Error !!!')
        return redirect('home:register')


class LoginView(View):
    __form = LoginForm

    def get(self, request):
        return render(request, 'authenticate/login.html', {'form': self.__form()})

    def post(self, request):
        if request.method == 'POST':
            form = self.__form(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                user = authenticate(request, username=username, password=password)
                if user:
                    login(request, user)
                    messages.success(request, 'User Login!!!')
                    return redirect('home:home')

        messages.warning(request, 'User Error!!!')
        return redirect('home:login')


def user_logout(request):
    logout(request)
    return redirect('home:login')
