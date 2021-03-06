from django.conf import settings

from django.conf.urls.static import static
from django.urls import include, path
from django.views.generic import TemplateView

from django.contrib import admin

from certviewer import views


urlpatterns = [
    path("", TemplateView.as_view(template_name="homepage.html"), name="home"),
    path("admin/", admin.site.urls),
    path("account/", include("account.urls")),
    path("certviewer/", include("certviewer.urls")),
    path('verify/<certificate_uid>', views.verify_award, name='verify_award')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
