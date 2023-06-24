from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt import views as jwt_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('thread.urls')),
    path('',include('chat.urls')),
    path('',include('report.urls')),
    path('',include('notification.urls')),
    path('',include('informations.urls')),
    path('',include('matcher.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
