from django.urls import path
from . import views
urlpatterns = [
    path('check/', views.compare_faces_view, name='health_check'),
    path('match-items/', views.match_items_view, name='match_items'),
    path('match-person/', views.match_person_view, name='match_person'),

]