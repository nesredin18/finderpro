from django.urls import path
from . import views
urlpatterns = [
    path('send-message/', views.sendmessage, name='send-message'),
    path('get-message/', views.getmessage, name='get-message'),
]