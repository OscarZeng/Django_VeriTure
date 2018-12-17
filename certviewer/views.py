from django.shortcuts import render
from django.http import Http404

from .models import Certificate
from .forms import JsonCertificateForm


def homepage(request):
    all_certificates = Certificate.objects.all()
    return render(request, 'certviewer_index.html', {'certs': all_certificates})


def award(request, certificate_uid):
    award = Certificate.objects.get(issuerID=certificate_uid)
    return render(request, 'award.html', {'award': award})


def json_award(request):
    context = {'title': "json_award"}
    return render(request, 'award.html', context)


def verify_award(request):
    context = {'title': "verify_award"}
    return render(request, 'dummy.html', context)


def intro(request):
    context = {'title': "intro"}
    return render(request, 'index.html', context)


def request(request):
    context = {'title': "request"}
    return render(request, 'request.html', context)


def faq(request):
    context = {'title': "faq"}
    return render(request, 'faq.html', context)


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
