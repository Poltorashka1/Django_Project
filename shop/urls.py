from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('<uuid:pk>', views.ClothesDetailView.as_view(), name='clothes_detail'),
]
