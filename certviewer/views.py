from django.shortcuts import render
from django.http import Http404

from .models import Certificate
from .models import JsonCertificate
from .forms import JsonCertificateForm

from cert_core.cert_model import model


def homepage(request):
    all_certificates = Certificate.objects.all()
    all_json_certificates = JsonCertificate.objects.all()
    return render(request, 'certviewer_index.html', {'certs': all_certificates, 'jsoncerts': all_json_certificates})


def display_award(request, certificate_uid):
    award = Certificate.objects.get(issuerID=certificate_uid)
    print(certificate_uid)
    #award(certificate_uid)
    #json_award = JsonCertificate.objects.get(issuerID=certificate_uid)
    #award = model.to_certificate_model(json_award.json)
    return render(request, 'award.html', {"award": award}) #award(certificate_uid))


def json_award(request):
    context = {'title': "json_award"}
    return render(request, 'award.html', context)


def verify_award(request, certificate_uid):
    from .verifier_bridge import verify
    verify_response = verify(certificate_uid)
    print(certificate_uid)
    print(verify_response)
    return render(request, 'dummy.html', {"context": verify_response})


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
