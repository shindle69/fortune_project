
from django.urls import path
from . import views

app_name = "yughyo"

urlpatterns = [
    path('<int:pk>/', views.iching),
    path('', views.front, name='yughyo_front'),
    path('new/', views.question, name='question_new'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('result/<int:pk>/', views.result, name='result'),
]
