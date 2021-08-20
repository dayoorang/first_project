from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from first_project import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accountapp.urls')),
    path('profiles/', include('profileapp.urls')),
    path('articles/', include('articleapp.urls')),
    path('comments/', include('commentapp.urls')),
    path('projects/', include('projectapp.urls')),
    path('subscribe/', include('subscribeapp.urls')),
  ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # docutment_root 경로를 뒤져서 MEDIA_URL 경로로 입력해주겠다라는 뜻.
