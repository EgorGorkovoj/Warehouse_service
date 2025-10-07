class LengthConstantsModels:
    """
    Базовый класс констант для ограничения длины символов полей модели.

    Атрибуты:
    - NAME_ORGANIZATION_LENGTH (int): Максимальная длина символов
      названия организации.
    - COUNTRY_LENGTH (int): Максимальная длина символов
      страны организации.
    - CITY_LENGTH (int): Максимальная длина символов названия
      города организации.
    - STREET_LENGTH (int): Максимальная длина символов названия
      улицы организации.
    - BUILDING_LENGTH (int): Максимальная длина символов номера
      здания организации.
    - CATEGORY_NAME_LENGTH (int): Максимальная длина символов
      названия категории.
    - PRODUCT_NAME_LENGTH (int): Максимальная длина символов поля
      наименования товара.
    - MIDDLE_NAME_LENGTH (int): Максимальная длина символов поля
      отчества модели пользователя.
    - POSTAL_CODE_LENGTH (int): Максимальная длина символов поля
      индекса модели пользователя.
    """

    NAME_ORGANIZATION_LENGTH: int = 200
    COUNTRY_LENGTH: int = 100
    CITY_LENGTH: int = 100
    STREET_LENGTH: int = 150
    BUILDING_LENGTH: int = 20
    CATEGORY_NAME_LENGTH: int = 255
    PRODUCT_NAME_LENGTH: int = 255
    MIDDLE_NAME_LENGTH: int = 50
    POSTAL_CODE_LENGTH: int = 20


class PriceConstants:
    """
    Базовый класс констант для цен товара в моделях.

    Атрибуты:
    - PRICE_NUMBER_OF_DIGITS (int): целая часть цены товара.
    - PRICE_FRACTIONAL_PART (int): сколько знаков после запятой у цены товара.
    """

    PRICE_NUMBER_OF_DIGITS: int = 10
    PRICE_FRACTIONAL_PART: int = 2


class DefaultValueConstants:
    """
    Базовый класс констант для значений по умолчанию.

    Атрибуты:
    - PRODUCT_QUANTITY (int): количество товара на складе.
    - ORDER_ITEM_QUANTITY (int): количество товара в заказе.
    """

    PRODUCT_QUANTITY: int = 0
    ORDER_ITEM_QUANTITY: int = 1
