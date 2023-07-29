from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage, message
from django.conf import settings
from django.contrib import messages


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


class BookingTemplateView(TemplateView):
    template_name = "booking.html"

    def post(self, request):
        bookingname = request.POST.get("booking-name")
        bookingemail = request.POST.get("booking-email")
        bookingphone = request.POST.get("booking-phone")
        bookingdate = request.POST.get("booking-date")
        bookingtime = request.POST.get("booking-time")
        bookingpeople = request.POST.get("booking-people")
        bookingmessage = request.POST.get("booking-message")

        messages.add_message(request, messages.SUCCESS,
                             f"Thanks {bookingname} for making an booking for the {bookingdate} at {bookingtime}, we will contact you to confirm as soon as possible")
        return HttpResponseRedirect(request.path)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = messages.get_messages(self.request)
        return context
