from django.contrib import admin
from django.urls import path, include
from login import views
import blogapp.urls
import blogapp.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.welcome, name='home'),
    path('blog/', include('blogapp.urls')),
    path('accounts/', include('allauth.urls')),
    path('login/', include('login.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
