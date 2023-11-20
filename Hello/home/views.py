from django.shortcuts import render          
from django.shortcuts import HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    #return HttpResponse("this is homepage")
    '''context = {
        'variable' : 'this is variable'
    }'''
    return render(request, 'index.html')
    messages.success(request,"this is a test msg")

def home(request):
     return render(request, 'index.html')
def about(request):
     return render(request, 'about.html')
def services(request):
    return render(request, 'services.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name') 
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name , email = email , phone = phone , desc = desc ,date = datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent !")

    return render(request, 'contact.html')
