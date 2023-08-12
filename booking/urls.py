from django.urls import path
from .views import (
    HomeTemplateView,
    BookingTemplateView,
    ManageBookingsTemplateView,
    admin_login,
    ConfirmedBookingsListView,
)

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('bookings/', BookingTemplateView.as_view(), name='booking'),
    path('manage/', ManageBookingsTemplateView.as_view(), name='manage'),
    path('admin/login/', admin_login, name='admin_login'),
    path('confirmed-bookings/', ConfirmedBookingsListView.as_view(),
         name='confirmed_bookings'),
]
