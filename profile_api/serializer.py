# Convertir objetos de Python, en informacion de JSON (y viceversa)
from rest_framework import serializers


class HelloSerializer(serializers.Serializer):

    # convierte/serializa un campo para probar nuestra APIView
    name = serializers.CharField(max_length=10)
