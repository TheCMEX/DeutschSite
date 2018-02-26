from django.conf.urls import url, include
from django.contrib import admin
from landing.views import homepage

urlpatterns = [
    url(r'^', homepage),
    url(r'^admin/', admin.site.urls),
]

