from django.db import models
from django.utils.translation import gettext_lazy as _

class SIM_NAO(models.TextChoices):
        SIM = 'SIM', _('Sim')
        NAO = 'NAO', _('Não')