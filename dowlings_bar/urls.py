from django.contrib import admin
from django.urls import path, include
from booking.views import admin_login, ManageBookingsTemplateView
admin_logout, CancelBookingView, EditBookingView

urlpatterns = [
    path('admin/login/', admin_login, name='admin_login'),
    path('admin/logout/', admin_logout, name='admin_logout'),
    path('admin/dashboard/',
         ManageBookingsTemplateView.as_view(), name='manage'),
    path('cancel_booking/<int:booking_id>/',
         CancelBookingView.as_view(), name='cancel_booking'),
    path('edit_booking/<int:booking_id>/',
         EditBookingView.as_view(), name='edit_booking'),
    path('admin/', admin.site.urls),
    path("", include("booking.urls")),
]
