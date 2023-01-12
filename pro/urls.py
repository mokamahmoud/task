
from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from task import urls as taskurls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(taskurls)),

    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
