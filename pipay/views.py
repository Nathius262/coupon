from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'pipay/home.html', {'loc': True,})

def dashboard_view(request):
    return render(request, 'pipay/dashboard.html')

def task_view(request):
    return render(request, 'pipay/task.html')

def couponVendor_view(request):
    return render(request, 'pipay/couponVendor.html')

def couponVerify_view(request):
    return render(request, 'pipay/couponVerify.html')
