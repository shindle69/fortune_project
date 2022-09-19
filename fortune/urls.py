
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('today_api/', include('today_api.urls', namespace="today_api")),
    path('my_today/', include('my_today.urls', namespace="my_today")),
    path('accounts/', include('accounts.urls', namespace="accounts")),
    path('yughyo/', include('yughyo.urls', namespace="yughyo")),
]
