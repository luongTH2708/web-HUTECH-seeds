from nav.models import Nav
from nav.serializers import Serializer
from rest_framework import generics


class List(generics.ListCreateAPIView):
    queryset = Nav.objects.all()
    serializer_class = Serializer


class Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nav.objects.all()
    serializer_class = Serializer