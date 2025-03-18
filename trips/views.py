# trips/views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Trip
from .serializers import TripSerializer
from .services.route_calculator import RouteCalculator

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    @action(detail=True, methods=['POST'])
    def calculate_route(self, request, pk=None):
        trip = self.get_object()
        calculator = RouteCalculator(trip)
        route_data = calculator.calculate_route()
        return Response(route_data)