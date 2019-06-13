from django.shortcuts import render
from certman.models import CertId, CertType, CertStatus, CertControl, CertScanUrl,CertScanRecord,CertManage,CertScanFile

from django.contrib.auth import  authenticate, login, logout
from django.http  import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required



def error_404(request):
        return render(request, 'certman/404.html', {})

def error_500(request):
        return render(request, 'certman/500.html', {})

# Create your views here.
@login_required
def dashboard(request):
    cert_records = CertScanRecord.objects.order_by('cert_hostname')
    cert_expired = CertScanRecord.objects.filter(cert_status__cert_status='expired').count()
    cert_alert = CertScanRecord.objects.filter(cert_status__cert_status='alert').count()
    cert_warning = CertScanRecord.objects.filter(cert_status__cert_status='warning').count()
    cert_total = CertScanRecord.objects.filter().count()
    cert_list = {'Record': cert_records, 'cert_expired': cert_expired, 'cert_alert': cert_alert, 'cert_warning': cert_warning, 'cert_total': cert_total}
    return render(request, "certman/index.html", context=cert_list)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('dashboard'))

def user_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        
        if  user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('dashboard'))
            
            else:
                return HttpResponse("Account  not  Active")
        else:
            print("Login Failed")
            return HttpResponse("invalid  login")
    else:
        return render(request, 'certman/login.html', {})


