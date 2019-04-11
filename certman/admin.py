from django.contrib import admin
from certman.models import ControlType, CertType, CertId, CertStatus, Record

# Register your models here.
admin.site.register(ControlType)
admin.site.register(CertType)
admin.site.register(CertId)
admin.site.register(CertStatus)
admin.site.register(Record)