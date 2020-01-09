from rest_framework.test import APITestCase

from .models import Shipment


class ShipmentTestCase(APITestCase):
    def setUp(self):
        self.title = 'tables'
        self.height_cm = 1.2
        self.weight = 10
        self.weight_lot_type = 'kg.'
        self.created_at = 'admin'
        self.shipment1 = Shipment.objects.create(
            title=self.title,
            height_cm=self.height_cm,
            weight=self.weight,
            weight_lot_type=self.weight_lot_type,
            author=self.created_at
        )

    def test_get_shipments(self):
        response = self.client.get('/shipments/', format='json')
        self.assertEqual(len(Shipment.objects.all()), 1)
        self.assertEqual(response.status_code, 200)

    def test_get_shipment(self):
        response = self.client.get('/shipments/1/', format='json')
        self.assertEqual(response.data['title'], 'tables')

    def test_create_shipment(self):
        self.client.post('/shipments/',
                         {'title': 'chairs',
                          'height_cm':'111',
                          'weight':'25',
                          'weight_lot_type':'lb.',
                          'author':"admin"},
                         format='json')
        self.assertEqual(len(Shipment.objects.all()), 2)

    def test_update_shipment(self):
        response = self.client.put('/shipments/1/',
                                   {'title': 'tables',
                                  'height_cm':'1.2',
                                  'weight':'10',
                                  'weight_lot_type':'kg.',
                                  'color': 'Other',
                                  'author':"admin"},
                                   format='json')
        self.assertEqual(response.status_code, 200)

    def test_delete_shipment(self):
        shipments_count_start = len(Shipment.objects.all())
        if shipments_count_start >= 1:
            self.client.delete('/shipments/1/')
            response = self.client.get('/shipments/1/', format='json')
            self.assertEqual(shipments_count_start, len(Shipment.objects.all())+1)
            self.assertEqual(response.status_code, 404)
