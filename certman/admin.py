from django.contrib import admin
from certman.models import CertId, CertType, CertStatus, CertControl, CertScanUrl, CertScanRecord, CertManage, CertScanFile

# Register your models here.
admin.site.register(CertId)
admin.site.register(CertType)
admin.site.register(CertStatus)
admin.site.register(CertControl)
admin.site.register(CertScanUrl)
admin.site.register(CertScanRecord)
admin.site.register(CertManage)
admin.site.register(CertScanFile)