from django.urls import path
from . import views
urlpatterns = [
    path('', views.getRoutes),
    path('thread/',views.fetch_all_data),
    path('thread/lost-person', views.getlostp),
    path('thread/post-lost-person', views.createlostp),
    path('thread/update-lost-person/<str:pk>/', views.updatelostp),
    path('thread/delete-lost-person/<str:pk>/', views.deletelostp),
    path('thread/lost-person/<str:pk>/', views.getlostpid),

    path('thread/found-person', views.getfoundp),
    path('thread/post-found-person', views.createfoundp),
    path('thread/update-found-person/<str:pk>/', views.updatefoundp),
    path('thread/delete-found-person/<str:pk>/', views.deletefoundp),
    path('thread/found-person/<str:pk>/', views.getfoundpid),

    path('thread/lost-item', views.getlosti),
    path('thread/lost-item/<str:pk>/', views.getlostiid),
    path('thread/post-lost-item', views.createlosti),
    path('thread/update-lost-item/<str:pk>/', views.updatelosti),
    path('thread/delete-lost-item/<str:pk>/', views.deletelosti),
    
    path('thread/found-item', views.getfoundi),
    path('thread/found-item/<str:pk>/', views.getfoundiid),
    path('thread/post-found-item', views.createfoundi),
    path('thread/update-found-item/<str:pk>/', views.updatefoundi),
    path('thread/delete-found-item/<str:pk>/', views.deletefoundi),   
    
    path('thread/wanted-person', views.getwantedp),
    path('thread/wanted-person/<str:pk>/', views.getwantedpid),
    path('thread/post-wanted-person', views.createwantedp),
    path('thread/update-wanted-person/<str:pk>/', views.updatewantedp),
    path('thread/delete-wanted-person/<str:pk>/', views.deletewantedp),
    

    path('login/',views.loginAccount),
    path('logout/',views.logoutAccount),
    path('register/',views.registeruser),
    path('verify-email/',views.VerifyEmail,name='emailverify'),
    path("sendvagian/", views.sendveriagian, name="send verification agian"),
    

    path('account/',views.getaccount),
    path('update-account',views.updateaccount),
    path('delete/',views.deleteaccount),
    path('account/<str:pk>/',views.getaccountid),
    path('forget-password/',views.forgetpassword,name='forgetpassword'),
    path('reset-password/',views.resetpassword,name='resetpassword'),
    path('change-password/',views.changepassword),

    path('my-post/',views.mypost),
    path('update-my-post/<str:pk>/',views.updatemypost),
    path('delete-my-post/<str:pk>/',views.deletemypost),

    path('post-near-you/',views.posts_near_you),
    path('fetch-all-data/',views.fetch_all_data),
    
    
   # path('log/',views.getThread),
    path('send/',views.send_otp),
   # path('token/',views.getwantedperson),
    
    
]