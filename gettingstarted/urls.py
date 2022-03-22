from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

from hello import views


urlpatterns = [
    path("", views.index, name="index"),
    path("category/<int:category_id_src>", views.category_page),
    path("product/<int:product_id_src>", views.product_page),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
