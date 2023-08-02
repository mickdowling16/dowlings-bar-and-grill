from django.contrib import admin
from django.urls import path, include
from booking.views import admin_login, ManageBookingsTemplateView, admin_logout

urlpatterns = [
    path('admin/login/', admin_login, name='admin_login'),
    path('admin/logout/', admin_logout, name='admin_logout'),
    path('admin/dashboard/', ManageBookingsTemplateView.as_view(), name='manage'),
    path('admin/', admin.site.urls),
    path("", include("booking.urls")),
]
