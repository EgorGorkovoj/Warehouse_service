from django.db import models


class BaseModel(models.Model):
    """
    Абстрактная модель.

    Назначение:
        Добавляет к модели дату создания и последнего изменения.

    Поля:
        created_at: Дата создания.
        updated_at: Дата изменения.
    """

    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now_add=False,
        auto_now=True
    )

    class Meta:
        abstract = True
