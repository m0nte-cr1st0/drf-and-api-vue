from django.db import models


COLOR_BLACK = 'Black'
COLOR_WHITE = 'White'
COLOR_RED = 'Red'
COLOR_OTHER = 'Other'

COLOR_CHOICES = (
    (COLOR_BLACK, 'Black'),
    (COLOR_WHITE, 'White'),
    (COLOR_RED, 'Red'),
    (COLOR_OTHER, 'Other'),
)


WEIGHT_LB = 'lb.'
WEIGHT_TON = 'ton'
WEIGHT_KG = 'kg.'
WEIGHT_G = 'g'

WEIGHT_CHOICES = (
    (WEIGHT_LB, 'lb.'),
    (WEIGHT_TON, 'ton'),
    (WEIGHT_KG, 'kg.'),
    (WEIGHT_G, 'g'),
)


class Shipment(models.Model):
    title = models.CharField(max_length=254)
    height_cm = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Height")
    weight = models.DecimalField(max_digits=7, decimal_places=2)
    weight_lot_type = models.CharField(max_length=10, choices=WEIGHT_CHOICES, default=WEIGHT_KG)
    color = models.CharField(max_length=10, choices=COLOR_CHOICES, default=COLOR_BLACK)
    author = models.CharField(max_length=254)

    def __str__(self):
        return 'Shipment: {}'.format(self.title)
