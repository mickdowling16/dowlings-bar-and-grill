from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage, message
from django.conf import settings


class HomeTemplateView(TemplateView):
    template_name = "index.html"
    
    def post(self, request):
        if request.method == 'POST':
            name = request.POST.get("name")
            email = request.POST.get("email")
            subject = request.POST.get("subject")
            message = request.POST.get("message")

            email = EmailMessage(
                subject=f"{name} has sent an enquiry about {subject}",
                body=f"{message}, This message was sent from {email}",
                from_email=settings.EMAIL_HOST_USER,
                to=[settings.EMAIL_HOST_USER],
                reply_to=[email]
            )
            email.send()
            return HttpResponse("Email sent successfully!")
        else:
            return HttpResponse("Invalid request method. Only POST requests are allowed.")

    

    
