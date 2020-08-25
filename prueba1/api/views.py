# from django.shortcuts import render
from .serializers import PersonaSerializer
from .models import Persona
from rest_framework import viewsets
# Create your views here.


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all().order_by('nombre')
    serializer_class = PersonaSerializer
