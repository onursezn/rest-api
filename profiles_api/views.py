from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    """testing APIview"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format = None):
        """returns a list of APIview feautures"""

        an_apiview = [
        "Uses HTTP methods as function(get, post, patch, put, delete)",
        "Is similar to a traditional Django view",
        "Gives you the most control over application logic",
        "Is mapped manually to URLs",
        ]

        return Response({"message": "Hello!", "an_apiview": an_apiview })


    def post(self, request):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})

        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handling updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handling partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        return Response({'method': 'DELETE'})



class HelloViewSet(viewsets.ViewSet):
    """test api view"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """ return a hello message"""

        a_viewset = [
        'USES ACTİONS (LİST,CREATE, RETRİEVE, UPDATE, PARTİAL_UPDATE)',
        'AUTOMATİCALLY MAPS TO URLS USİNG ROUTES',
        'PROVİDES MORE FUNCTİONALİTY WİTH LESS CODE'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})

        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """handle getting an object by its ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile,)
