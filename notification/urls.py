from django.urls import path
from . import views
urlpatterns = [
    path('getnotfication/', views.getnotfication),
]