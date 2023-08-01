from django.urls import path, include
from .views import HomeTemplateView, BookingTemplateView, ManageBookingsTemplateView, admin_login

urlpatterns = [
    path("", HomeTemplateView.as_view(), name="home"),
    path("bookings/", BookingTemplateView.as_view(), name="booking"),
    path("manage/", ManageBookingsTemplateView.as_view(), name="manage"),
    path('admin/login/', admin_login, name='admin_login'),
]
