from django.urls import path
from .views import AppointmentListCreateView, AppointmentRetrieveUpdateDestroyView
from .views import (
    ActiveAppointmentListView,
    ExpiredAppointmentListView,
    AppointmentRetrieveUpdateDestroyView,
    TimeSlotListCreateView,
    TimeSlotDeleteView,
    UserProfileRetrieveUpdateView,
    ChangePasswordView,
)

urlpatterns = [
    path('appointments/', AppointmentListCreateView.as_view(), name='appointment-list-create'),
    path('appointments/<int:pk>/', AppointmentRetrieveUpdateDestroyView.as_view(), name='appointment-detail'),
    path('appointments/active/', ActiveAppointmentListView.as_view(), name='active-appointments'),
    path('appointments/expired/', ExpiredAppointmentListView.as_view(), name='expired-appointments'),
    path('timeslots/', TimeSlotListCreateView.as_view(), name='timeslot-list-create'),
    path('timeslots/<int:pk>/', TimeSlotDeleteView.as_view(), name='timeslot-delete'),
    path('profile/', UserProfileRetrieveUpdateView.as_view(), name='profile-retrieve-update'),
    path('profile/change-password/', ChangePasswordView.as_view(), name='change-password'),
]
