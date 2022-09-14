from django.views.generic import ListView
from . import models


# Create your views here.
class HomePageView(ListView):
    model = models.Shop
    template_name = 'shop/home.html'
