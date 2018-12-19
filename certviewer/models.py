from django.db import models
from account.models import Account

# Create your models here.


class Certificate (models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    logoImg = models.CharField(max_length=8000)
    text = models.CharField(max_length=1000)
    issuerID = models.CharField(max_length=1000)
    chain = models.CharField(max_length=500)
    transactionID = models.CharField(max_length=200)
    transactionIDURL = models.URLField
    issuedOn = models.CharField(max_length=100)
    signatureImg = models.CharField(max_length=8000)
    subtitle = models.CharField(max_length=300)

    def __str__(self):
        return self.name;

# this is the certificate file in json form


class JsonCertificate (models.Model):
    issuerID = models.CharField(max_length=1000)
    json = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.issuerID;

