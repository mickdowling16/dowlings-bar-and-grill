from django.urls import path, include
from .views import HomeTemplateView, BookingTemplateView, ManageBookingsTemplateView

urlpatterns = [
    path("", HomeTemplateView.as_view(), name="home"),
    path("bookings/", BookingTemplateView.as_view(), name="booking"),
    path("manage-bookings/", ManageBookingsTemplateView.as_view(),
         name="manage"),
]
