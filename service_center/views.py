
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Customer, Vehicle, Mechanic, ServiceBooking
from .serializers import (
    CustomerSerializer,
    VehicleSerializer,
    MechanicSerializer,
    ServiceBookingSerializer,
    
)

class CustomerListCreateView(APIView):

    # Get all customers
    def get(self, request):
        qs = Customer.objects.all()
        serializer_instance = CustomerSerializer(qs, many=True)
        return Response(data=serializer_instance.data)

    # Add a new customer
    def post(self, request):
        form_data = request.data
        serializer_instance = CustomerSerializer(data=form_data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(
                data=serializer_instance.data,
                status=status.HTTP_201_CREATED
            )

        else:
            return Response(
                data=serializer_instance.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        

from django.shortcuts import get_object_or_404


class CustomerRetrieveUpdateDeleteView(APIView):

    def get(self, request, pk):
        customer = get_object_or_404(Customer, id=pk)
        serializer_instance = CustomerSerializer(customer)
        return Response(data=serializer_instance.data)

    def put(self, request, pk):
        customer = get_object_or_404(Customer, id=pk)
        serializer_instance = CustomerSerializer(
            customer,
            data=request.data
        )

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(
                data=serializer_instance.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, pk):
        customer = get_object_or_404(Customer, id=pk)
        customer.delete()
        return Response(
            {"message": "Customer deleted successfully"},
            status=status.HTTP_200_OK
        )



class VehicleListCreateView(APIView):

    # Get all vehicles
    def get(self, request):
        qs = Vehicle.objects.all()
        serializer_instance = VehicleSerializer(qs, many=True)
        return Response(data=serializer_instance.data)

    # Add a new vehicle
    def post(self, request):
        form_data = request.data
        serializer_instance = VehicleSerializer(data=form_data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(
                data=serializer_instance.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                data=serializer_instance.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        

class VehicleRetrieveUpdateDeleteView(APIView):

    # Get a single vehicle
    def get(self, request, pk):
        vehicle = get_object_or_404(Vehicle, id=pk)
        serializer_instance = VehicleSerializer(vehicle)
        return Response(data=serializer_instance.data)

    # Update vehicle details
    def put(self, request, pk):
        vehicle = get_object_or_404(Vehicle, id=pk)
        serializer_instance = VehicleSerializer(
            vehicle,
            data=request.data
        )

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(
                data=serializer_instance.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    # Delete a vehicle
    def delete(self, request, pk):
        vehicle = get_object_or_404(Vehicle, id=pk)
        vehicle.delete()
        return Response(
            {"message": "Vehicle deleted successfully"},
            status=status.HTTP_200_OK
        )



class MechanicListCreateView(APIView):

    # Get all mechanics
    def get(self, request):
        qs = Mechanic.objects.all()
        serializer_instance = MechanicSerializer(qs, many=True)
        return Response(data=serializer_instance.data)

    # Add a new mechanic
    def post(self, request):
        form_data = request.data
        serializer_instance = MechanicSerializer(data=form_data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(
                data=serializer_instance.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                data=serializer_instance.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class MechanicRetrieveUpdateDeleteView(APIView):

    # Get a single mechanic
    def get(self, request, pk):
        mechanic = get_object_or_404(Mechanic, id=pk)
        serializer_instance = MechanicSerializer(mechanic)
        return Response(data=serializer_instance.data)

    # Update mechanic details
    def put(self, request, pk):
        mechanic = get_object_or_404(Mechanic, id=pk)
        serializer_instance = MechanicSerializer(
            mechanic,
            data=request.data
        )

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(
                data=serializer_instance.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    # Delete a mechanic
    def delete(self, request, pk):
        mechanic = get_object_or_404(Mechanic, id=pk)
        mechanic.delete()
        return Response(
            {"message": "Mechanic deleted successfully"},
            status=status.HTTP_200_OK
        )



class ServiceBookingListCreateView(APIView):

    # Get all service bookings
    def get(self, request):
        qs = ServiceBooking.objects.all()
        serializer_instance = ServiceBookingSerializer(qs, many=True)
        return Response(data=serializer_instance.data)

    # Create a new service booking
    def post(self, request):
        form_data = request.data
        serializer_instance = ServiceBookingSerializer(data=form_data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(
                data=serializer_instance.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                data=serializer_instance.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        

class ServiceBookingRetrieveUpdateDeleteView(APIView):

    # Get a single booking
    def get(self, request, pk):
        booking = get_object_or_404(ServiceBooking, id=pk)
        serializer_instance = ServiceBookingSerializer(booking)
        return Response(data=serializer_instance.data)

    # Update booking details
    def put(self, request, pk):
        booking = get_object_or_404(ServiceBooking, id=pk)
        serializer_instance = ServiceBookingSerializer(
            booking,
            data=request.data
        )

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(
                data=serializer_instance.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    # Delete a booking
    def delete(self, request, pk):
        booking = get_object_or_404(ServiceBooking, id=pk)
        booking.delete()
        return Response(
            {"message": "Service booking deleted successfully"},
            status=status.HTTP_200_OK
        )


