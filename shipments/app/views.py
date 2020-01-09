from decimal import Decimal

from django.http import HttpResponse
from rest_framework import viewsets

from .models import Shipment
from .serializers import ShipmentSerializer


class ShipmentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer

    def get_renderer_context(self):
        context = super().get_renderer_context()
        action = self.action
        if (action == 'retrieve'):
            context['shipments'] = Shipment.objects.all()
        elif (action == 'list'):
            context['shipments'] = Shipment.objects.all()
        return context

    def put(self, request, *args, **kwargs):
        data = request.data
        shipment = Shipment.objects.get(id=int(data['id']))
        if data.get('title'):
            shipment.title = data['title']
        if data.get('height_cm'):
            shipment.height_cm = Decimal(data['height_cm'])
        if data.get('weight'):
            shipment.weight = Decimal(data['weight'])
        if data.get('weight_lot_type'):
            shipment.weight_lot_type = data['weight_lot_type']
        if data.get('color'):
            shipment.color = data['color']
        if data.get('author'):
            shipment.author = data['author']
        shipment.save()
        return HttpResponse()

    def delete(self, request, *args, **kwargs):
        shipment = Shipment.objects.get(id=int(request.data['id']))
        shipment.delete()
        return HttpResponse()
