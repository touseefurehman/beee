from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('began_admin/', admin.site.urls),
    path('admin/', include('began_admin.urls')),
    path('',include('main.urls'))
]
