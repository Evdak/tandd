from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView, RedirectView
from django.urls import reverse_lazy
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = "T&D"
admin.site.site_title = "T&D Админпанель"
admin.site.index_title = "T&D Админпанель"

urlpatterns = [
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
