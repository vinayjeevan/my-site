from django.contrib import admin
from django.urls import path,include
#from app_site.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_site/',include('app_site.urls')),
    #path('',home)
    
]
