from django.contrib import admin
from django.urls import path, include
from main.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('post/', include('post.urls', namespace='post')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('accounts/', include('allauth.urls')),
]
