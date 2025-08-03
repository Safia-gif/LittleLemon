from rest_framework.decorators import api_view
from .models import Menu, Booking
from .serializers import MenuSerializer,BookingSerializer
from rest_framework import generics, viewsets

# Create your views here. 
class MenuView(generics.ListCreateAPIView):
   queryset = Menu.objects.all()
   serializer_class = MenuSerializer

class SingleMenuView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
  queryset = Menu.objects.all()
  serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
   queryset = Booking.objects.all()
   serializer_class = BookingSerializer