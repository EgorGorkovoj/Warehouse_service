from django.db import models

from core.constants import LengthConstantsModels


class Supplier(models.Model):
    """
    Модель поставщика.

    Назначение:
        Хранит информацию о поставщике, включая его организацию, местоположение и адрес.

    Поля:
        name_organization: Наименование организации.
        country: Страна поставщика.
        city: Город поставщика.
        street: Улица поставщика.
        building: Номер здания.
    """

    name_organization = models.CharField(
        verbose_name='Наименование организации',
        max_length=LengthConstantsModels.NAME_ORGANIZATION_LENGTH
    )
    country = models.CharField(
        verbose_name='Страна',
        max_length=LengthConstantsModels.COUNTRY_LENGTH
    )
    city = models.CharField(
        verbose_name='Город',
        max_length=LengthConstantsModels.CITY_LENGTH
    )
    street = models.CharField(
        verbose_name='Улица',
        max_length=LengthConstantsModels.STREET_LENGTH
    )
    building = models.CharField(
        verbose_name='Здание',
        max_length=LengthConstantsModels.BUILDING_LENGTH
    )

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.name_organization
