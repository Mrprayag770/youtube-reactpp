from django.shortcuts import render, HttpResponse
from datetime import datetime
# Create your views here.
from home.models import Contact
from django.contrib import messages


def index(request):
    context = {
        'variable': 10,
        'variable1': 20
    }
    return render(request, 'index.html', context)

    # return HttpResponse("this is homee page")


def about(request):
    return render(request, 'about.html')


def bill(request):
    return render(request, 'bill.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobno = request.POST.get('mobno')
        passw = request.POST.get('passw')
        contact = Contact(name=name, email=email, mobno=mobno,
                          passw=passw)
        contact.save()
        messages.success(request, "data assded to db :)")
    return render(request, 'contact.html')
