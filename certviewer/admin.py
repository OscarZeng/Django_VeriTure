from django.contrib import admin
from .models import Certificate
from .models import JsonCertificate
# Register your models here.

admin.site.register(Certificate)
admin.site.register(JsonCertificate)