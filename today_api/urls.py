
from django.urls import path
from . import views

app_name = "today_api"

urlpatterns = [
    path('',  views.today_catch,),
    path('about/', views.about, name='about'),
    path('<int:pk>/', views.today12),
    path('today/', views.today_catch, name='today'),
]
