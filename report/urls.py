from django.urls import path
from . import views
urlpatterns = [
    path('report/', views.sendmessage, name='send-message'),
]