
from django.urls import path
from . import views

app_name = "my_today"

urlpatterns = [
    path('', views.mytoday, name='mytoday'),
]
