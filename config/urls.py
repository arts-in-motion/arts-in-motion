from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url('^', admin.site.urls),
    url('^api/', include('portal.api.urls')),
]
