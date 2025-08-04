from .models import Menu, Booking
from rest_framework import serializers
from django.contrib.auth.models import User

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
       password = serializers.CharField(
            min_length=8, # Example: set a minimum length
            write_only=True,
            required=True,
            style={'input_type': 'password'}
        )
       class Meta:
            model = User
            fields = ['id', 'username','password', 'email'] # Customize fields as needed

