from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def customer(request):
    return render(request, 'customer.html')

def distributor(request):
    return render(request, 'distributor.html')

def chaincode(request):
    return render(request, 'chaincode.html')