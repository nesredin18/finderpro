from django.urls import path
from . import views
urlpatterns = [
    path('matcher/', views.compare_images, name='matcher'),
    path('health-check/', views.health_check, name='health_check'),
    path('match-items/', views.match_items_view, name='match_items'),
]