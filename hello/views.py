from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.core.mail import message, send_mail

from .models import Greeting


# Create your views here.
def index(request):
    if request.method == "POST":
        form_name = request.POST['form-name']
        form_number = request.POST['form-number']
        form_email = request.POST['form-email']
        form_subject = request.POST['form-subject']
        form_message = request.POST['form-message']

        # Send Email
        send_mail(
            form_subject,
            form_message,
            form_email,
            ['mail.teciq@gmail.com']
        )

        return render(request, "index.html", {"form_name": form_name})
    else:
        # return HttpResponse('Hello from Python!')
        return render(request, "index.html")

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
