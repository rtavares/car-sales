from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Car
from .serializers import CarSerializer


class UserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data["token"])
        return Response({"token": token.key, "user_id": token.user_id})


class CarListViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.filter(display=True).all()
    serializer_class = CarSerializer


class CarCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarSingleRetrieveAPIView(RetrieveAPIView):
    queryset = Car.objects.filter(display=True).all()
    serializer_class = CarSerializer
