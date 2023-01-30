from django.conf import settings
from django.urls import path
from accounts import views

app_name = "about"

urlpatterns = [    
    path('profile/<int:pk>/', views.profile, name='profile'),
    # path('profile', views.profile, name='profile'),
]
