from django.shortcuts import render
from django.http import Http404

from .models import Certificate
from .models import JsonCertificate
from .forms import JsonCertificateForm

from .verifier_bridge import verify

def homepage(request):
    all_certificates = Certificate.objects.all()
    all_json_certificates = JsonCertificate.objects.all()
    return render(request, 'certviewer_index.html', {'certs': all_certificates, 'jsoncerts': all_json_certificates})


def display_award(request, certificate_uid):
    # from . import cert_store
    # award = cert_store.get_certificate(certificate_uid)
    # print(award)

    from certviewer.certificate_store_bridge import award
    Award = award(certificate_uid)
    #verify_response = verify(certificate_uid)
    all_certificates = Certificate.objects.all()
    print(Award)
    return render(request, 'award.html', {"award": Award,
                                          "certificate_uid": certificate_uid, 'certs': all_certificates}) #award(certificate_uid))


def json_award(request):
    context = {'title': "json_award"}
    return render(request, 'award.html', context)


def verify_award(request, certificate_uid):

    verify_response = verify(certificate_uid)
    # from cert_verifier import verifier
    # from cert_core.cert_model import model
    # JsonAward = JsonCertificate.objects.get(issuerID=certificate_uid)
    # award = model.to_certificate_model(JsonAward.json)
    # print(award)
    # verify_response = verifier.verify_certificate(award)
    # print(certificate_uid)
    print(verify_response)
    return render(request, 'verification.html', {"verification_info": verify_response, "certificate_uid": certificate_uid})


def intro(request):
    context = {'title': "intro"}
    return render(request, 'index.html', context)


def request(request):
    context = {'title': "request"}
    return render(request, 'request.html', context)


def faq(request):
    return render(request, 'faq.html')


def bitcoinkeys(request):
    context = {'title':"bitcoinkeys"}
    return render(request, 'bitcoinkeys.html', context)


def issuer(request):
    context = {'title': "issuer"}
    return render(request, 'dummy.html', context)


def spec(request):
    context = {'title': "spec"}
    return render(request, 'dummy.html', context)


def upload(request):
    form = JsonCertificateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {
        "form": form,
    }
    return render(request, 'upload.html', context)
