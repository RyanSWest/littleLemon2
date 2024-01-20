from django.shortcuts import render
from .models import Menu, Booking, User

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView
from rest_framework.decorators import api_view, permission_classes
from .serializers import MenuSerializer, UserSerializer, BookingSerializer
# Create your views here.
@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})

def index(request):
    return render(request, 'index.html', {})


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class MenuItemsView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Menu.objects.all().order_by('price')
    serializer_class = MenuSerializer
    
class SingleMenuItemView(RetrieveUpdateDestroyAPIView ):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all().order_by('booking_date')
    serializer_class = BookingSerializer