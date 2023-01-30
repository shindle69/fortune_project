
from django.contrib import admin
from django.urls import path, include
from today_api import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('today_api/', include('today_api.urls', namespace="today_api")),
    path('my_today/', include('my_today.urls', namespace="my_today")),
    path('accounts/', include('accounts.urls', namespace="accounts")),
    path('yughyo/', include('yughyo.urls', namespace="yughyo")),
    path('about/', include('about.urls', namespace="about")),
    path('fortune_board/', include('fortune_board.urls', namespace="fortune_board")),

    path('', views.today_catch)
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)