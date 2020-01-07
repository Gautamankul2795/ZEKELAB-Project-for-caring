from django.shortcuts import render
from django.http import HttpResponse
from .models import Caretaker, Careneeder, Contact


# Create your views here.
def index(request):
    return render(request, 'care/index.html')


def caretaker(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        dob = request.POST.get('dob', '')
        milestone = request.POST.get('milestone', '')
        review = request.POST.get('review', '')
        message = request.POST.get('message')
        care = Caretaker(name=name, email=email, phone=phone, dob=dob, milestone=milestone, review=review,
                         message=message)
        care.save()

    return render(request, 'care/caretaker.html')


def careneeder(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        dob = request.POST.get('dob', '')
        payee = request.POST.get('payee', '')
        require = request.POST.get('require')
        need = Careneeder(name=name, email=email, phone=phone, dob=dob, payee=payee, require=require)
        need.save()

    return render(request, 'care/careneeder.html')


def aboutus(request):
    return render(request, 'care/aboutus.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact_us = Contact(name=name, email=email, phone=phone, desc=desc)
        contact_us.save()
    return render(request, 'care/contact.html')


def search(request):
    data = Caretaker.objects.all()
    caretakerdata = {
        "care_num": data
    }

    return render(request, 'care/search.html', caretakerdata)
