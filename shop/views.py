from django.views.generic import ListView, DetailView
from . import models


# Create your views here.
class HomePageView(ListView):
    model = models.Shop
    template_name = 'shop/home.html'
    context_object_name = 'clothes_list'


class ClothesDetailView(DetailView):
    model = models.Shop
    template_name = 'shop/clothes_info.html'
    context_object_name = 'clothes_detail'
