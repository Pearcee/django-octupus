from django.conf import settings
from django.db import models
from django.utils import timezone


class Tariffs(models.Model):
    value_inc_vat = models.DecimalField(max_digits=3, decimal_places=2)
    valid_from = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.value_inc_vat

      

""" 
"value_exc_vat": 9.03,
"value_inc_vat": 9.4815,
"valid_from": "2021-02-26T22:30:00Z",
"valid_to": "2021-02-26T23:00:00Z"

"""