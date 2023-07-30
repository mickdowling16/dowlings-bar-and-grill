from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage, message
from django.conf import settings
from django.contrib import messages
from .models import Bookings
from django.core.paginator import Paginator
import datetime
from django.template import Context
from django.template.loader import render_to_string, get_template


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

        booking = Bookings.objects.create(
            name=bookingname,
            email=bookingemail,
            phone=bookingphone,
            date=bookingdate,
            time=bookingtime,
            people=bookingpeople,
            message=bookingmessage,
        )

        booking.save()

        messages.add_message(request, messages.SUCCESS,
                             f"Thanks {bookingname} for making a booking for the {bookingdate} at {bookingtime}, we will contact you to confirm as soon as possible")
        return HttpResponseRedirect(request.path)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = messages.get_messages(self.request)
        return context


class ManageBookingsTemplateView(TemplateView):
    template_name = "manage-bookings.html"
    login_required = True

    def post(self, request):
        date = request.POST.get("date")
        time = request.POST.get("time")
        booking_id = request.POST.get("booking-id")
        booking = Bookings.objects.get(id=booking_id)
        booking.accepted = True
        booking.accepted_date = datetime.datetime.now()
        booking.save()

        data = {
            "name": booking.name,
            "date": date,
            "time": time,
        }

        message = get_template('email.html').render(data)
        email = EmailMessage(
            "About your booking at Dowling's Bar & Grill",
            message,
            settings.EMAIL_HOST_USER,
            [booking.email],
        )
        email.content_subtype = "html"
        email.send()

        messages.add_message(request, messages.SUCCESS,
                             f"You accepted the booking of {booking.name}")
        return HttpResponseRedirect(request.path)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        bookings = Bookings.objects.all()

        per_page = 3
        paginator = Paginator(bookings, per_page)
        page_number = self.request.GET.get('page', 1)
        bookings = paginator.get_page(page_number)

        context.update({
            "bookings": bookings,
            "title": "Manage Bookings"
        })
        return context
