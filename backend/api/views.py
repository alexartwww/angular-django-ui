from django.shortcuts import render
from api.models import Hero
from rest_framework import viewsets
from api.serializers import HeroSerializer


class HeroViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Hero.objects.all().order_by('id')
    serializer_class = HeroSerializer
