from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView, RedirectView
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from django.contrib import messages
from .models import Bookings
from django.core.paginator import Paginator
import datetime
from django.template.loader import get_template
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from datetime import timedelta
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db.models import Sum
from django.http import JsonResponse


class HomeTemplateView(TemplateView):
    template_name = "index.html"
    title = "Homepage"

    def post(self, request):
        if request.method == 'POST':
            name = request.POST.get("name")
            email = request.POST.get("email")
            subject = request.POST.get("subject")
            message = request.POST.get("message")

            # send email with contact form information to restuarant
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

        # Defining the maximum capacity allowed per 30-minute slot
        max_capacity_per_slot = 20

        booking_date = datetime.datetime.strptime(
            bookingdate, "%Y-%m-%d").date()
        booking_time = datetime.datetime.strptime(bookingtime, "%H:%M").time()

        # Calculate the end time of the booking
        end_time = (datetime.datetime.combine(datetime.date(1, 1, 1), booking_time) +
                    datetime.timedelta(minutes=int(bookingpeople) * 30)).time()

        # Calculate the total number of people already booked for the given time slot
        total_people_booked = Bookings.objects.filter(
            date=booking_date,
            time__range=(booking_time, end_time)
        ).aggregate(Sum('people'))['people__sum'] or 0

        # Calculate the remaining capacity for the time slot
        remaining_capacity = max_capacity_per_slot - total_people_booked

        if remaining_capacity >= int(bookingpeople):
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
        else:
            messages.add_message(request, messages.WARNING,
                                 "Sorry, there are no available bookings for this time slot, please try an alternative time.")

        return HttpResponseRedirect(request.path)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = messages.get_messages(self.request)
        return context


class ManageBookingsTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "manage-bookings.html"
    login_required = True
    login_url = '/admin_login/'

    def post(self, request):
        action = request.POST.get("action")
        booking_id = request.POST.get("booking-id")
        booking = get_object_or_404(Bookings, id=booking_id)

        try:
            if action == "accept":
                booking.accepted = True
                booking.accepted_date = datetime.datetime.now()
                booking.save()

                data = {
                    "name": booking.name,
                    "date": booking.date,
                    "time": booking.time,
                }
                # email customer to confirm booking time and date using email.html template
                message = get_template('email.html').render(data)
                email = EmailMessage(
                    "About your booking at Dowling's Bar & Grill",
                    message,
                    settings.EMAIL_HOST_USER,
                    [booking.email],
                )
                email.content_subtype = "html"
                email.send()

                # success message when booking confirmed
                messages.add_message(request, messages.SUCCESS,
                                     f"You accepted the booking of {booking.name}")

            elif action == "suggest_time":
                date = request.POST.get("date")
                time = request.POST.get("time")
                booking.suggested_date = date
                booking.suggested_time = time
                booking.date = date
                booking.time = time
                booking.save()

                data = {
                    "name": booking.name,
                    "date": booking.suggested_date,
                    "time": booking.suggested_time,
                }

                # email customer with new suggested time using email_suggested_time.html template
                message = get_template(
                    'email_suggested_time.html').render(data)
                email = EmailMessage(
                    "Update about your booking at Dowling's Bar & Grill",
                    message,
                    settings.EMAIL_HOST_USER,
                    [booking.email],
                )
                email.content_subtype = "html"
                email.send()

                bookings = Bookings.objects.filter(
                    accepted=False).order_by('date')
                context = self.get_context_data(unconfirmed_bookings=bookings)
                self.request.session['django_timezone'] = 'UTC'
                context.update({
                    "unconfirmed_bookings": bookings,
                    "title": "Manage Bookings"
                })

                messages.add_message(request, messages.INFO,
                                     f"You suggested a new time for the booking of {booking.name}. An email will be sent to the customer.")

                return render(request, self.template_name, context)
        # messages for error handling for validation
        except ValidationError as ve:
            messages.add_message(request, messages.ERROR,
                                 f"Validation error occurred: {ve}")
        except Exception as e:
            messages.add_message(
                request, messages.ERROR, f"An error occurred while sending the email: {e}")

        return HttpResponseRedirect(reverse('manage'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        bookings = Bookings.objects.filter(accepted=False).order_by('date')

        # pagination to show only 9 bookings per page
        per_page = 9
        paginator = Paginator(bookings, per_page)
        page_number = self.request.GET.get('page', 1)
        bookings_page = paginator.get_page(page_number)

        context.update({
            "unconfirmed_bookings": bookings_page,
            "title": "Manage Bookings"
        })
        return context


def admin_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active and user.is_superuser:
                login(request, user)
                return redirect('/manage/')
    else:
        form = AuthenticationForm()

    return render(request, 'admin/admin_login.html', {'form': form})


def admin_logout(request):
    logout(request)
    return redirect('home')


class ConfirmedBookingsListView(LoginRequiredMixin, ListView):
    model = Bookings
    login_required = True
    template_name = 'confirmed_bookings.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        if self.request.GET.get('clear_filters'):
            return super().get_queryset().filter(
                accepted=True).order_by('date')

        today = timezone.now().date()
        date_filter = self.request.GET.get('date')

        if date_filter:
            try:
                date_filter = timezone.datetime.strptime(
                    date_filter, '%Y-%m-%d').date()
                queryset = super().get_queryset().filter(
                    accepted=True, date=date_filter).order_by('date')
            except ValueError:
                queryset = super().get_queryset().filter(
                    accepted=True, date__gte=today - timedelta(days=1)).order_by('date')
        else:
            queryset = super().get_queryset().filter(
                accepted=True, date__gte=today - timedelta(days=1)).order_by('date')

        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        per_page = 9
        paginator = Paginator(self.object_list, per_page)
        page_number = self.request.GET.get('page', 1)
        bookings_page = paginator.get_page(page_number)

        context.update({
            "bookings": bookings_page,
            "title": "Confirmed Bookings"
        })
        return context


class UnconfirmedBookingsListView(LoginRequiredMixin, ListView):
    model = Bookings
    login_required = True
    template_name = 'manage-bookings.html'
    context_object_name = 'bookings'
    queryset = Bookings.objects.filter(accepted=False)


class CancelBookingView(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        booking_id = kwargs['booking_id']
        booking = get_object_or_404(Bookings, id=booking_id)
        booking.delete()

        data = {
            "name": booking.name,
            "date": booking.date,
            "time": booking.time,
        }

        message = get_template('email_cancel_booking.html').render(data)
        email = EmailMessage(
            "Cancellation of your booking at Dowling's Bar & Grill",
            message,
            settings.EMAIL_HOST_USER,
            [booking.email],
        )
        email.content_subtype = "html"
        email.send()

        messages.success(
            self.request, "Booking has been canceled successfully!")

        return reverse('confirmed_bookings')


class EditBookingView(LoginRequiredMixin, TemplateView):
    template_name = 'edit_booking.html'
    login_required = True

    def get(self, request, booking_id):
        booking = get_object_or_404(Bookings, id=booking_id)
        context = {'booking': booking}
        return render(request, self.template_name, context)

    def post(self, request, booking_id):
        booking = get_object_or_404(Bookings, id=booking_id)

        try:
            booking.name = request.POST.get("name")
            booking.email = request.POST.get("email")
            booking.phone = request.POST.get("phone")
            booking.date = request.POST.get("date")
            booking.time = request.POST.get("time")
            booking.people = request.POST.get("people")
            booking.message = request.POST.get("message")
            booking.save()

            messages.add_message(request, messages.SUCCESS,
                                 f"The booking for {booking.name} has been updated.")
            return redirect('confirmed_bookings')

        except ValidationError as ve:
            messages.add_message(request, messages.ERROR,
                                 f"Validation error occurred: {ve}")
            return redirect('edit_booking', booking_id=booking_id)
        except Exception as e:
            messages.add_message(
                request, messages.ERROR, f"An error occurred while updating the booking: {e}")
            return redirect('edit_booking', booking_id=booking_id)
