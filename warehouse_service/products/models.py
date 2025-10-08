from django.db import models

from core.constants import (DefaultValueConstants,
                            LengthConstantsModels,
                            PriceConstants)
from core.models import BaseModel
from suppliers.models import Supplier


class Category(models.Model):
    """
    Модель категории товаров.

    Назначение:
        Хранит информацию о категориях и подкатегориях товаров,
        позволяя формировать древовидную структуру (иерархию категорий).

    Поля:
        name: Название категории.
        parent_category: Родительская категория
                         (если категория является подкатегорией).
    """
    name = models.CharField(
        verbose_name='Название категории',
        max_length=LengthConstantsModels.CATEGORY_NAME_LENGTH
    )
    parent_category = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='subcategories'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(BaseModel):
    """
    Модель товара.

    Назначение:
        Хранит информацию о товаре, включая его наименование,
        поставщика, категорию и цену.

    Поля:
        name: Наименование товара.
        supplier: Поставщик, у которого закупается товар.
        category: Категория, к которой относится товар.
        price_per_unit: Цена за единицу товара.

    Наследуемые поля от абстрактной модели BaseModel:
        created_at: Дата создания.
        updated_at: Дата изменения.
    """

    name = models.CharField(
        verbose_name='Наименование товара',
        max_length=LengthConstantsModels.PRODUCT_NAME_LENGTH
    )
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Поставщик'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Категория товара'
    )
    price_per_unit = models.DecimalField(
        verbose_name='Цена за единицу товара',
        max_digits=PriceConstants.PRICE_NUMBER_OF_DIGITS,
        decimal_places=PriceConstants.PRICE_FRACTIONAL_PART
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name']

    def __str__(self):
        return self.name


class RemainingStock(models.Model):
    """
    Модель остатка товара на складе.

    Назначение:
        Хранит информацию о текущем количестве конкретного товара на складе.

    Поля:
        product: Ссылка на товар
                 (у каждого товара может быть только один остаток).
        quantity: Количество товара, доступное на складе.
    """
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name='stock',
        verbose_name='Товар на складе'
    )
    quantity = models.PositiveIntegerField(
        verbose_name='Количество товара на складе',
        default=DefaultValueConstants.PRODUCT_QUANTITY
    )

    class Meta:
        verbose_name = 'Остаток на складе'
        verbose_name_plural = 'Остатки на складе'

    def __str__(self):
        return f'{self.product.name}: {self.quantity} шт.'
