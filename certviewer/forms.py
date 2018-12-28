from django import forms

from .models import JsonCertificate
from .models import Certificate


class JsonCertificateForm(forms.ModelForm):
    class Meta:
        model = JsonCertificate
        fields = [
            "account",
            "issuerID",
            "json"
        ]


class CertificateForm(forms.ModelForm):
    model = Certificate
    fields = [
        "account",
        "name",
        "title",
        "organization",
        "logoImg",
        "text",
        "issuerID",
        "chain",
        "transactionID",
        "transactionIDURL",
        "issuedOn",
        "signatureImg",
        "subtitle"
    ]
