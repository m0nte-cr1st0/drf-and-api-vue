from rest_framework import serializers
from .models import Shipment


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = '__all__'

    def validate_height_cm(self, value):
        if float(value) or int(value):
            if value > 0:
                return value
            else:
                raise serializers.ValidationError("Enter positive number.")
