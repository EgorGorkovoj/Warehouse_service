from django.contrib.auth.models import AbstractUser
from django.db import models

from core.constants import LengthConstantsModels


class Customer(AbstractUser):
    """
    Модель покупателя (клиента), расширяющая стандартную
    модель пользователя Django.

    Назначение:
        Хранит информацию о пользователе,
        включая личные данные и адрес проживания.

    Поля (унаследованные от AbstractUser):
        username: Имя пользователя для входа.
        password: Захешированный пароль.
        first_name: Имя.
        last_name: Фамилия.
        email: Электронная почта.
        is_active: Статус активности.
        is_staff: Признак персонала (доступ к админке).
        is_superuser: Признак суперпользователя.
        date_joined: Дата регистрации пользователя.

    Дополнительные поля:
        middle_name: Отчество пользователя.
        age: Возраст пользователя.
        country: Страна проживания.
        street: Улица (название улицы).
        building: Номер дома.
        apartment: Номер квартиры.
        postal_code: Почтовый индекс.
    """

    middle_name = models.CharField(
        verbose_name='Отчество',
        max_length=LengthConstantsModels.MIDDLE_NAME_LENGTH,
        blank=True,
        null=True
    )
    age = models.PositiveIntegerField(
        verbose_name='Возраст',
        blank=True,
        null=True
    )
    country = models.CharField(
        verbose_name='Страна',
        max_length=LengthConstantsModels.COUNTRY_LENGTH,
        blank=True,
        null=True
    )
    street = models.CharField(
        verbose_name='Улица',
        max_length=LengthConstantsModels.STREET_LENGTH,
        blank=True,
        null=True
    )
    building = models.CharField(
        verbose_name='Дом',
        max_length=LengthConstantsModels.BUILDING_LENGTH,
        blank=True,
        null=True
    )
    apartment = models.CharField(
        verbose_name='Квартира',
        max_length=LengthConstantsModels.APARTMENT_LENGTH,
        blank=True,
        null=True
    )
    postal_code = models.CharField(
        verbose_name='Почтовый индекс',
        max_length=LengthConstantsModels.POSTAL_CODE_LENGTH,
        blank=True,
        null=True
    )

    def __str__(self):
        full_name = f'{self.last_name or ''} ' \
                    f'{self.first_name or ''} ' \
                    f'{self.middle_name or ''}'.strip()
        return full_name if full_name else self.username

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'
