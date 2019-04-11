from django.db import models


# Create your models here.
class CertId(models.Model):
    cert_id = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.cert_id


class CertStatus(models.Model):
    cert_status = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.cert_status


class CertType(models.Model):
    cert_type = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.cert_type


class CertControl(models.Model):
    cert_control = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.cert_control


class CertScanFile(models.Model):
    cert_id = models.ForeignKey(CertId, on_delete=models.PROTECT)
    cert_hostname = models.CharField(max_length=255)
    cert_service = models.CharField(max_length=255)
    cert_platform = models.CharField(max_length=255)
    cert_data = models.TextField()

    def __str__(self):
        return self.cert_hostname


class CertScanUrl(models.Model):
    cert_id = models.ForeignKey(CertId, on_delete=models.PROTECT)
    cert_hostname = models.CharField(max_length=255)
    cert_port = models.IntegerField()
    cert_service = models.CharField(max_length=255)
    cert_platform = models.CharField(max_length=255)

    def __str__(self):
        return self.cert_hostname


class CertManage(models.Model):
    cert_scan_range = models.CharField(max_length=255)
    cert_port_range = models.CharField(max_length=255)

    def __str__(self):
        return '%s %s' % (self.cert_scan_range, self.cert_port_range)


class CertScanRecord(models.Model):
    control_type = models.ForeignKey(CertControl, on_delete=models.PROTECT)
    cert_type = models.ForeignKey(CertType, on_delete=models.PROTECT)
    cert_id = models.ForeignKey(CertId, on_delete=models.PROTECT)
    cert_hostname = models.CharField(max_length=255)
    cert_scan_port = models.CharField(max_length=255)
    cert_app_owner = models.CharField(max_length=255)
    cert_platform = models.CharField(max_length=255)
    cert_issuer = models.CharField(max_length=255)
    cert_cn = models.CharField(max_length=255)
    cert_status = models.ForeignKey(CertStatus, on_delete=models.PROTECT)
    cert_days = models.IntegerField()
    cert_date = models.DateField()

    def __str__(self):
        return self.cert_hostname
