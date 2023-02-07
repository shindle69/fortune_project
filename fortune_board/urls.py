from django.urls import path
from . import views

app_name = "fortune_board"

urlpatterns = [    
    
    path('search/<str:q>/', views.PostSearch.as_view()),
    path('tag/<str:slug>/', views.tag_page),
    path('category/<str:slug>/', views.category_page),
    path('', views.PostList.as_view(), name="post_list"),
    path('<int:pk>/', views.PostDetail.as_view(),),    
    path('<int:pk>/new_comment/', views.new_comment),
    path('create_post/', views.PostCreate.as_view()),
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),
    path('update_comment/<int:pk>/', views.CommentUpdate.as_view()),
    path('delete_comment/<int:pk>/', views.delete_comment),
    # path('', views.index, name='fortune_board'),
    # path('<int:pk>/', views.single_post_page),
    # path('profile', views.profile, name='profile'),
]
