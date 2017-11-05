from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url('^', admin.site.urls),
    url('^api/', include('portal.api.urls')),
    url('^grappelli/', include('grappelli.urls')),
    url('^export_action/', include("export_action.urls",
                                   namespace="export_action")),
]
