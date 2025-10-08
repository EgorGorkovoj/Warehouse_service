from django.db import models

from core.constants import PriceConstants, DefaultValueConstants
from products.models import Product
from users.models import Customer


class Order(models.Model):
    """
    Модель заказа.

    Назначение:
        Хранит информацию о заказе, включая клиента и дату оформления.

    Поля:
        customer: Клиент, оформивший заказ.
        order_date: Дата и время оформления заказа
                    (устанавливается автоматически).
    """

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='Клиент'
    )
    order_date = models.DateTimeField(
        verbose_name='Дата заказа',
        auto_now_add=True
    )

    def __str__(self):
        return f'Заказ {self.id} от {self.customer}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-order_date']


class OrderItem(models.Model):
    """
    Промежуточная модель для связи заказов (Order) и товаров (Product).

    Назначение:
        Реализует связь многие-ко-многим между заказами и товарами, храня
        дополнительные данные: количество и цену на момент покупки.

    Поля:
        order: Заказ, к которому относится данный товар.
        product: Товар, входящий в заказ.
        quantity: Количество единиц товара в заказе.
        purchase_price: Цена за единицу товара на момент покупки.

    Ограничения:
        Уникальность комбинации заказа и товара (не допускается дублирование
        товара в одном заказе).
    """

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='Заказ'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='order_items',
        verbose_name='Товар'
    )
    quantity = models.PositiveIntegerField(
        verbose_name='Количество',
        default=DefaultValueConstants.ORDER_ITEM_QUANTITY
    )
    purchase_price = models.DecimalField(
        verbose_name='Цена покупки',
        max_digits=PriceConstants.PRICE_NUMBER_OF_DIGITS,
        decimal_places=PriceConstants.PRICE_FRACTIONAL_PART
    )

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказа'
        constraints = [
            models.UniqueConstraint(
                fields=['order', 'product'], name='unique_order_product'
            ),
        ]

    def __str__(self):
        return f'{self.product.name} — {self.quantity} шт. (заказ №{self.order.id})'
