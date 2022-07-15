from django.db import models
from .boolean_response import SIM_NAO

class MLModel(models.Model):
    distance_home = models.DecimalField(max_digits = 8, decimal_places = 2)
    distance_last = models.DecimalField(max_digits = 8, decimal_places = 2)
    value         = models.DecimalField(max_digits = 8, decimal_places = 2)
    same_seller   = models.CharField(max_length = 3, choices=SIM_NAO.choices, default = 0)
    physical      = models.CharField(max_length = 3, choices=SIM_NAO.choices, default = 0)
    password      = models.CharField(max_length = 3, choices=SIM_NAO.choices, default = 0)
    online        = models.CharField(max_length = 3, choices=SIM_NAO.choices, default = 0)