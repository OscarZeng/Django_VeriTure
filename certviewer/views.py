from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def homepage(request):
    #template = loader.get_template('./templates/user.html')
    #return HttpResponse (template.render(request))
    messages = {'title': "homepage"}
    return render (request, 'index.html', messages)


def award(request):
    context = {'title': "award"}
    return render(request, 'award.html', context)


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
