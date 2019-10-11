from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

admin.sites.AdminSite.site_header = settings.ADMIN_SITE_HEADER
admin.sites.AdminSite.site_title = settings.ADMIN_SITE_TITLE
admin.sites.AdminSite.index_title = settings.ADMIN_INDEX_TITLE


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/menu/", include("menu.api.urls")),
]
