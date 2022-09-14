from django.views.generic import CreateView
from . import forms
from django.urls import reverse_lazy


# Create your views here.
class SignupPageView(CreateView):
    form_class = forms.CustomUserCreationForms
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
