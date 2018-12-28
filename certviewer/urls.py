from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

# all the commented links are existing links from the Flask Version, currently is not very useful here.
urlpatterns = [
    path('', views.homepage, name='homepage'),

    path('upload', views.upload, name='upload'),

    path('verify/<certificate_uid>', views.verify_award, name='verify_award'),

    # path('intro', views.intro, name='intro'),

    # path('request', views.request, name='request'),

    path('faq', views.faq, name='faq'),

    # path('bitcoinkeys', views.bitcoinkeys, name='bitcoinkeys'),

    # path('issuer/issuer_file', views.issuer, name='issuer'),

    # path('spec', views.spec, name='spec'),

    path('certificate/<certificate_uid>', views.json_award, name='json_award'),

    path('<certificate_uid>', views.display_award, name='award')

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.CERT_URL, document_root=settings.CERT_ROOT)
    urlpatterns += static(settings.CERT_URL, document_root=settings.CERT_ROOT)
