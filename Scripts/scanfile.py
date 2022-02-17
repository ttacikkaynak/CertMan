import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dashboard.settings')

import django

django.setup()
import signal
import sys
from certman import getssl
from certman.importrecord import  updateCert
from certman.models import CertScanFile



def signal_handler(sig, frame):
        print('Scan stopped.')
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)




def scanFile(host, service, platform, certificate):
    detail_cert = getssl.getfile_certificate(certificate)
    updateCert(detail_cert, host, "-", "File Control", "Web Server")



def getfilerecords():
    file = CertScanFile.objects.values_list()
    scanfile = list(file)
    for i in range(len(scanfile)):
        host = scanfile[i][2]
        service = scanfile[i][3]
        platform = scanfile[i][4]
        certificate = scanfile[i][5]
        detail_cert = scanFile(str(host), str(service), str(platform), str(certificate))