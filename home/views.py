from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse

from category.models import Category
from home.forms import ContactForm, SignupForm, LoginForm, UserUpdateForm, ProfileUpdateForm
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['category'] = Category.objects.all()

        return context


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


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'u_form': user_form,
            'p_form': profile_form,
        }

        return render(request, 'user/profile.html', context)

    def post(self, request):
        user_form = UserUpdateForm(
            request.POST,
            instance=request.user
        )

        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request, 'User Profile Updated!!!')

            return redirect('home:home')

        else:
            messages.warning(request, 'Error Updated Profile!!!')

            return redirect('home:home')
