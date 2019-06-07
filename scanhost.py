import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dashboard.settings')

import django

django.setup()
from netaddr import *
import socket
import signal
import sys
import getssl
from importrecord import updateCert
from certman.models import CertManage, CertScanUrl, CertScanFile



def signal_handler(sig, frame):
        print('Scan stopped.')
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


def lookup(addr):
    try:
        data = socket.gethostbyaddr(str(addr))
        host = repr(data[0])
        host = str(host)
        host = host.strip("'")
        return host
    except:
        return "NA"


def isOpen(ip, port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
       s.settimeout(0.3)
       s.connect((ip, int(port)))
       s.shutdown(2)
       return True
   except:
       return False



def scanNetwork(host, port):
    for ip in IPSet([host]):
        if (isOpen(str(ip), str(port))):
            try:
                detail_cert = getssl.detail_certificate(str(ip), str(port))
                print("OK-Connection", str(ip))
                updateCert(detail_cert, ip, port, "Port Control", "Web Server")
            except:
                detail_cert=['SSL Check Error', 'SSL Check Error', 0, 0, '0', '0', 'SSL Check Error', '0']

        else:
            print("NOK", str(ip))


def getrecords():
    network = CertManage.objects.values_list()
    network = list(network)
    for i in range(len(network)):
        host = network[i][1]
        port = network[i][2]
        detail_cert = scanNetwork(str(host), str(port))

getrecords()