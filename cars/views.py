from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Car
from .serializers import CarSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    @action(detail=True, methods=['get'])
    def get_photo(self, request, pk=None):
        car = get_object_or_404(Car, pk=pk)
        if car.photo:
            return Response({'photo_url': request.build_absolute_uri(car.photo.url)})
        return Response({'error': 'Фото отсутствует'}, status=404)
