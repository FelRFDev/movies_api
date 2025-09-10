from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Actor
from .serializers import ActorSerializer
from core.permissions import GlobalDefaultPermission

# Create your views here.
class ActorListCreateView(ListCreateAPIView):
    authentication_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    authentication_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
