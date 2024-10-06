from rest_framework import serializers

from .models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = (
            "id",
            "owner",
            "model",
            "brand",
            "year",
            "color",
            "seats",
            "type",
            "price",
            "display",
            "publishing_date",
        )
