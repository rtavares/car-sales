from django.urls import path

from .views import (
    CarCreateAPIView,
    CarListViewSet,
    CarSingleRetrieveAPIView,
    UserLoginView,
)

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("cars/", CarListViewSet.as_view({"get": "list"}), name="car-list"),
    path("car/<int:pk>/", CarSingleRetrieveAPIView.as_view(), name="car-detail"),
    path("car/create/", CarCreateAPIView.as_view(), name="car-create"),
]
