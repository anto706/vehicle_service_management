
from django.urls import path

from .views import (
    CustomerListCreateView,
    CustomerRetrieveUpdateDeleteView,
    VehicleListCreateView,
    MechanicListCreateView,
    ServiceBookingListCreateView,
    VehicleRetrieveUpdateDeleteView,
    MechanicRetrieveUpdateDeleteView,
    ServiceBookingRetrieveUpdateDeleteView,
)



urlpatterns = [
    path('customers/', CustomerListCreateView.as_view()),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDeleteView.as_view()),

    path('vehicles/', VehicleListCreateView.as_view()),
    path('vehicles/<int:pk>/', VehicleRetrieveUpdateDeleteView.as_view()),

    path('mechanics/', MechanicListCreateView.as_view()),
    path('mechanics/<int:pk>/', MechanicRetrieveUpdateDeleteView.as_view()),

    path('bookings/', ServiceBookingListCreateView.as_view()),
    path('bookings/<int:pk>/', ServiceBookingRetrieveUpdateDeleteView.as_view()),
]

