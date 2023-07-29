from django.urls import path, include
from .views import HomeTemplateView, BookingTemplateView

urlpatterns = [
    path("", HomeTemplateView.as_view(), name="home"),
    path("bookings/", BookingTemplateView.as_view(), name="booking"),
]
