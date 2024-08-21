from django.urls import path
from . import views

urlpatterns = [
    path('plans/', views.subscription_plans, name='subscription_plans'),
    path('content/', views.content_list, name='content_list'),
]
