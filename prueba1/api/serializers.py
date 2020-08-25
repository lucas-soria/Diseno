from rest_framework import serializers
from .models import Persona


class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Persona
        fields = ('nombre', 'apellido')
