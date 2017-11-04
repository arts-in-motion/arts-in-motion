from django.contrib import admin
from django.contrib.sites.models import Site


admin.site.site_header = "Arts in Motion Data Portal"
admin.site.site_title = "Arts in Motion"
admin.site.site_url = None  # Hide "view site" link
admin.site.index_title = None  # Hide default "Site administration" text

admin.site.unregister(Site)
