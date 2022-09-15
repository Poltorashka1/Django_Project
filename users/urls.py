from django.urls import path
from . import views

urlpatterns = [
    path('accounts/password/change/', views.CustomPasswordChange.as_view(), name='account_password_change')
]
