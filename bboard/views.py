from .models import Bb
from .serializers import BbSerializer
from rest_framework import generics


class BbListCreate(generics.ListCreateAPIView):
    queryset=Bb.objects.all()
    serializer_class=BbSerializer
