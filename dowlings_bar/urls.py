from django.contrib import admin
from django.urls import path, include
from booking.views import (
    ManageBookingsTemplateView,
    admin_logout,
    CancelBookingView,
    EditBookingView,
    admin_login,
    error_404,
    error_403,
)

urlpatterns = [
    path('admin/login/', admin_login, name='admin_login'),
    path('admin/logout/', admin_logout, name='admin_logout'),
    path('admin/dashboard/', ManageBookingsTemplateView.as_view(), name='manage'),
    path('cancel_booking/<int:booking_id>/',
         CancelBookingView.as_view(), name='cancel_booking'),
    path('edit_booking/<int:booking_id>/',
         EditBookingView.as_view(), name='edit_booking'),
    path('admin/', admin.site.urls),
    path('', include('booking.urls')),
]

# Define error handlers
handler404 = error_404
handler403 = error_403

# Add a catch-all URL pattern to handle any unmatched paths
urlpatterns += [
    path('<path:invalid_path>/', error_404, name='invalid_path'),
]
