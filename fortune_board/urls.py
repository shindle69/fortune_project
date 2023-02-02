from django.urls import path
from . import views

app_name = "fortune_board"

urlpatterns = [    
    path('category/<str:slug>/', views.category_page),
    path('', views.PostList.as_view(), name="post_list"),
    path('<int:pk>/', views.PostDetail.as_view(),),
    # path('', views.index, name='fortune_board'),
    # path('<int:pk>/', views.single_post_page),
    # path('profile', views.profile, name='profile'),
]
