from django.shortcuts import render
from certman.models import CertId, CertType, CertStatus, CertControl, CertScanUrl,CertScanRecord,CertManage,CertScanFile


# Create your views here.
def index(request):
    cert_records = CertScanRecord.objects.order_by('cert_hostname')
    cert_expired = CertScanRecord.objects.filter(cert_status__cert_status='expired').count()
    cert_alert = CertScanRecord.objects.filter(cert_status__cert_status='alert').count()
    cert_warning = CertScanRecord.objects.filter(cert_status__cert_status='warning').count()
    cert_total = CertScanRecord.objects.filter().count()
    cert_list = {'Record': cert_records, 'cert_expired': cert_expired, 'cert_alert': cert_alert, 'cert_warning': cert_warning, 'cert_total': cert_total}
    return render(request, "certman/index.html", context=cert_list)


def dashboard(request):
    cert_records = CertScanRecord.objects.order_by('cert_hostname')
    cert_list = {'Record': cert_records}
    return render(request, "certman/index.html", context=cert_list)