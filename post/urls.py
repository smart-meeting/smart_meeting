from django.urls import path
from .views import *

app_name = 'post'

urlpatterns = [
    path('', tables, name='tables'),
    path('', table_new, name='table_new'),
    path('detail/<int:pk>/', table_detail, name='table_detail'),
    path('join/<int:pk>/', join, name='join'),
    path('unjoin/<int:pk>/', unjoin, name='unjoin'),
]