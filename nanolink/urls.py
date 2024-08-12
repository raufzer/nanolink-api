
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from apps.shortner.views import Redirector

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.shortner.urls')),    
    path('<str:nano_link>', Redirector.as_view(), name='redirector'),
]
