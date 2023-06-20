from django.urls import path
from . import views
urlpatterns = [
    path('get-about/', views.getabout, name='get about'),
    path('get-contact/', views.getcontact, name='get contact'),
    path('get-privacy/', views.getprivacy, name='get privacy'),
    path('get-term/', views.getterm, name='get term'),
    path('get-faq/', views.getfaq, name='get faq'),
    path('get-region/', views.getregion, name='get region'),
    path('get-city/', views.getcity, name='get city'),
    path('create-contact/', views.createcontact, name='create contact'),
    
]