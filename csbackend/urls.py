from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve as mediaserve
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("product.urls", namespace="product")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
else:
    urlpatterns += [re_path(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$',mediaserve, {'document_root':settings.MEDIA_ROOT}),re_path(f'^{settings.STATIC_URL.lstrip("/")}(?P<path>.*)$',mediaserve, {'document_root':settings.STATIC_ROOT}),]
