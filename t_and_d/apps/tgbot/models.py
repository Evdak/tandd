from django.db import models


class TGUser(models.Model):
    tg_id = models.BigIntegerField(
        'ID в Telegram',
        default=0,
    )

    name = models.CharField(
        'Ник в Telegram',
        max_length=255,
    )

    is_admin = models.BooleanField(
        'Админ',
        default=False,
    )

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "Клиент в TG"
        verbose_name_plural = "Клиенты в TG"
