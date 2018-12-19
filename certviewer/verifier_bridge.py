from cert_verifier import verifier
from .models import JsonCertificate


def verify(certificate_uid):
    print("verifier_bridge > verify has been called")
    from . import cert_store
    certificate = cert_store.get_certificate(certificate_uid)
    # from cert_core.cert_model import model
    # json_certificate = JsonCertificate.objects.filter(issuerID=certificate_uid)
    # certificate = model.to_certificate_model(json_certificate)
    if certificate:
        # A walk around to set default etherscan api token as '' to avoid
        # TypeError in composing ethesan URL. The options can be removed
        # when https://github.com/blockchain-certificates/cert-verifier/pull/21
        # is deployed.
        options={'etherscan_api_token':''}
        verify_response = verifier.verify_certificate(certificate, options=options)
        print(verify_response)
        return verify_response
    else:
        raise Exception('Cannot find certificate with uid=%s', certificate_uid)
