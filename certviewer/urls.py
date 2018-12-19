from django.urls import path
from django.conf.urls import url
from django.conf import  settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),

    path('upload', views.upload, name='upload'),

    # url(r'^(?P<certificate_uid>[str]+)$', views.display_award, name='award'),
    path('<certificate_uid>', views.display_award, name='award'),

    path('certificate/<certificate_uid>', views.json_award, name='json_award'),

    path('verify/<certificate_uid>', views.verify_award, name='verify_award'),

    path('intro', views.intro, name='intro'),

    path('request', views.request, name='request'),

    path('faq', views.faq, name='faq'),

    path('bitcoinkeys', views.bitcoinkeys, name='bitcoinkeys'),

    path('issuer/issuer_file', views.issuer, name='issuer'),

    path('spec', views.spec, name='spec')


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.CERT_URL, document_root=settings.CERT_ROOT)
