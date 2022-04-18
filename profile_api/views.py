from email import message
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profile_api import serializer
# Create your views/controllers here.

# 'HelloApiTest' titulo de la peticion al verlo en django framework


class HelloApiTestView(APIView):
    # API View de prueba

    serializer_class = serializer.HelloSerializer

    def get(self, req, format=None):
        # retornar caracteristicas de API View
        list_apiView = ['Usamos metodos de HTTP como funciones ()get, put, patch, post, delete',
                        'es similar a una vista (controlador) tradicional',
                        'Nos da el mayor control sobre la logica de nuestra aplicacion',
                        'esta mapeado manualmente a los URLs']
        return Response({'title': 'test', 'message': list_apiView})

    def post(self, req):
        # crea un mensaje con nuestro nombre
        serializer = self.serializer_class(data=req.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, req, pk=None):
        # Actualizar un objeto completo
        return Response({'method': 'PUT'})

    def patch(self, req, pk=None):
        # Actualizar un campo en especifico del objeto
        return Response({'method': 'PATCH'})

    def delete(self, req, pk=None):
        # Borrar un objeto
        return Response({'method': 'DELETE'})
