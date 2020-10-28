from django.shortcuts import render
from hashids import Hashids
from .models import DigitalContent

def index(request):
    return render(request, 'index.html')

def customer(request):
    context = {
            'files': [
                {
                    'file_name': 'file 001.jpg',
                    'hash_id': '3567892',
                    'date_created': '20/10/2020'
                },
                {
                    'file_name': 'file 001.jpg',
                    'hash_id': '3567892',
                    'date_created': '20/10/2020'
                }                
            ]
    }
    return render(request,"customer.html",context)
    
def distributor(request):
    #files = DigitalContent.objects.all()  
    context = {
            'files': [
                {
                    'file_name': 'file 001.jpg',
                    'hash_id': '3567892',
                    'date_created': '20/10/2020'
                },
                {
                    'file_name': 'file 001.jpg',
                    'hash_id': '3567892',
                    'date_created': '20/10/2020'
                }                
            ]
    }
    return render(request,"distributor.html",context)

def create_digital_content(request):
    #hashid = hashids.encode(file_name)
    pass

def blockchain(request):
    context = {
            'logs': [
                {                    
                    'log_id': '3567892',
                    'content': 'This blog post shows a few different types of content that is supported and styled with Bootstrap. Basic typography, images, and code are all supported.',
                    'date_created': '20/10/2020'
                },
                {
                    'log_id': '3567892',
                    'content': 'This blog post shows a few different types of content that is supported and styled with Bootstrap. Basic typography, images, and code are all supported.',
                    'date_created': '20/10/2020'
                }                
            ]
    }
    return render(request,"blockchain.html",context)