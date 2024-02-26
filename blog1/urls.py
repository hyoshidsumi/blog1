from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('note/', include('app2.urls')),
    path('', include('app1.urls')),
]
