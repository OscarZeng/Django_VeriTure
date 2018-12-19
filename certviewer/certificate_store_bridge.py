from .models import Certificate
from .models import JsonCertificate
from cert_core import cert_store
from . import certificate_formatter


def award(certificate_uid):
    print ("certificate_store_bridge > award has been called.")
    requested_format = JsonCertificate.objects.get(issuerID=certificate_uid)
    if requested_format == 'json':
        return get_award_json(certificate_uid)
    award, verification_info = certificate_formatter.get_formatted_award_and_verification_info(cert_store,
                                                                                               certificate_uid)
    return {'award': award,
            'verification_info': verification_info}


def get_award_json(certificate_uid):
    print("certificate_store_bridge > get_award_json has been called.")
    certificate_json = cert_store.get_certificate_json(certificate_uid)
    return certificate_json
