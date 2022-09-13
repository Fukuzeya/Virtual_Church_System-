from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Management.urls',namespace='management')),
    path('dashboard/',include('Dashboard.urls', namespace='dashboard')),
    path('Online-conference/', include('video.urls',namespace='video')),
    path('Online/payments/',include('Payments.urls',namespace='payment')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
