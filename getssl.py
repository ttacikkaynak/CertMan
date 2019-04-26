import ssl
import socket
import OpenSSL
from datetime import datetime


def get_certificate(host, port, timeout=0.5):
    ssl._create_default_https_context = ssl._create_unverified_context
    context = ssl._create_default_https_context()
    conn = socket.create_connection((host, port))
    sock = context.wrap_socket(conn, server_hostname=host)
    sock.settimeout(timeout)
    try:
        der_cert = sock.getpeercert(True)
    finally:
        sock.close()
    return ssl.DER_cert_to_PEM_cert(der_cert)


def detail_certificate(host, port):
    date_now = datetime.now()
    detail_cert = []
    certificate = get_certificate(host, port)
    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, certificate)
    cert_cn = x509.get_subject().CN
    cert_issuer = x509.get_issuer().CN
    cert_serial = x509.get_serial_number()
    cert_notBefore = datetime.strptime(x509.get_notBefore().decode('ascii'), '%Y%m%d%H%M%SZ')
    cert_notAfter = datetime.strptime(x509.get_notAfter().decode('ascii'), '%Y%m%d%H%M%SZ')
    cert_days = (cert_notAfter - date_now).days
    detail_cert.extend((cert_cn, cert_issuer, cert_serial, cert_days, str(cert_notBefore), str(cert_notAfter), certificate, str(date_now)))
    return detail_cert


def getfile_certificate(certificate):
    date_now = datetime.now()
    detail_cert = []
    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, certificate)
    cert_cn = x509.get_subject().CN
    cert_issuer = x509.get_issuer().CN
    cert_serial = x509.get_serial_number()
    cert_notBefore = datetime.strptime(x509.get_notBefore().decode('ascii'), '%Y%m%d%H%M%SZ')
    cert_notAfter = datetime.strptime(x509.get_notAfter().decode('ascii'), '%Y%m%d%H%M%SZ')
    cert_days = (cert_notAfter - date_now).days
    detail_cert.extend((cert_cn, cert_issuer, cert_serial, cert_days, str(cert_notBefore), str(cert_notAfter), certificate, str(date_now)))
    return detail_cert