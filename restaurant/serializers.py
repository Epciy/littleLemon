from django.contrib.auth.models import User
from .models import MenuItem,TableBooking
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['url','email','username','groups']

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id','title','price','inventory']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableBooking
        fields = "__all__"
