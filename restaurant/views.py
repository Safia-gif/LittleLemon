from rest_framework.decorators import api_view
from .models import Menu, Booking
from .serializers import MenuSerializer,BookingSerializer,UserSerializer
from rest_framework import generics, viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render

# Create your views here.
def index(request):
 return render(request, 'index.html', {})

# Create your views here. 
class MenuView(generics.ListCreateAPIView):
   
   queryset = Menu.objects.all()
   serializer_class = MenuSerializer

class SingleMenuView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
  queryset = Menu.objects.all()
  serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
   permission_classes = [IsAuthenticated]
   queryset = Booking.objects.all()
   serializer_class = BookingSerializer

class UserViewSet(viewsets.ModelViewSet):
        queryset = User.objects.all()
        serializer_class = UserSerializer