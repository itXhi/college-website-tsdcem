from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from college_app import views  # Import your views directly here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing, name='landing'),
    path('home/', views.website_home, name='home'),
    path('download/fees/', views.download_fees, name='download_fees'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)