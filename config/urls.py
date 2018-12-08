from django.conf.urls import url, include
from django.contrib import admin
from portal.core import views


urlpatterns = [
    url('^', admin.site.urls),
    url('^api/', include('portal.api.urls')),
    url('^grappelli/', include('grappelli.urls')),
    url('^export_action/', include("export_action.urls",
                                   namespace="export_action")),
    url(r'^class-reports/$', views.class_reports, name='class_reports'),
    url(
        r'^class-reports/(?P<class_id>[^/]+)$',
        views.detail_class_reports,
        name="detail_class_reports"
    )
]
