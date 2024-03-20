from django.contrib import admin
from django.urls import path

from nutrients.urls import nutrients_urls

urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns += nutrients_urls
