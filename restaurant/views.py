from django.shortcuts import render

from django.contrib.auth.models import User
from .models import MenuItem,TableBooking
from .serializers import UserSerializer,MenuItemSerializer,BookingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
#from django.views.generic import View
from rest_framework import viewsets,  generics
# Create your views here.

# static HTML content
def home(request):
    return render(request,"home.html")

@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})



class UserViewSet(viewsets.ModelViewSet):
   permission_classes = [IsAuthenticated] 
    
   queryset = User.objects.all()
   serializer_class = UserSerializer
   

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
     

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class BookingView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = TableBooking.objects.all()
    serializer_class = BookingSerializer