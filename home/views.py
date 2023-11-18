
from django.shortcuts import render, redirect
from django.http import HttpResponse

from home.forms import ContactForm
from django.views.generic import CreateView, View
from django.views.generic.edit import FormMixin


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



class ContactView(View, FormMixin):
    # form_class = ContactForm
    form_class = ContactForm
    
    def get(self, request, *args, **kwargs):
        form = ContactForm()

        return render(request, 'home/contact.html', {'form': form})
    

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        return redirect('contact')