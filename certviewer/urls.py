from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),

    path('certificate_uid', views.award, name='award'),

    path('certificate/certificate_uid', views.json_award, name='json_award'),

    path('verify/certificate_uid', views.verify_award, name='verify_award'),

    path('intro', views.intro, name='intro'),

    path('request', views.request, name='request'),

    path('faq', views.faq, name='faq'),

    path('bitcoinkeys', views.bitcoinkeys, name='bitcoinkeys'),

    path('issuer/issuer_file', views.issuer, name='issuer'),

    path('spec', views.spec, name='spec'),

    path('upload', views.upload, name='upload')

]