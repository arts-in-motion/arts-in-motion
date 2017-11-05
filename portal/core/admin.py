from django.contrib import admin
from django.contrib.sites.models import Site


admin.site.site_url = None  # Hide "view site" link
admin.site.index_title = "Home"

admin.site.unregister(Site)
