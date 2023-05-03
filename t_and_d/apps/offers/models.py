from django.db import models
from django.utils.safestring import mark_safe


class OfferPhoto(models.Model):
    file = models.ImageField('Файл с фото', upload_to='offer_photo')

    def image_preview(self):
        return mark_safe(
            str(self)
        )

    def __str__(self) -> str:
        return '<img src="{url}"  style="width: 12vw; height: auto;" />'.format(
            url=self.file.url,
            width=self.file.width,
            height=self.file.height,
        )

    class Meta:
        verbose_name = "Фото объектов"
        verbose_name_plural = "Фото объектов"


class OfferPhotoMain(models.Model):
    file = models.ImageField('Файл с фото', upload_to='offer_photo_main')

    def image_preview(self):
        return mark_safe(
            str(self)
        )

    def __str__(self) -> str:
        return '<img src="{url}"  style="width: 12vw; height: auto;" />'.format(
            url=self.file.url,
            width=self.file.width,
            height=self.file.height,
        )

    class Meta:
        verbose_name = "Фото объектов главные"
        verbose_name_plural = "Фото объектов главные"


class OfferPhotoPlan(models.Model):
    file = models.ImageField('Файл с фото', upload_to='offer_photo_plan')

    def image_preview(self):
        return mark_safe(
            str(self)
        )

    def __str__(self) -> str:
        return '<img src="{url}"  style="width: 12vw; height: auto;" />'.format(
            url=self.file.url,
            width=self.file.width,
            height=self.file.height,
        )

    class Meta:
        verbose_name = "Фото планов объектов"
        verbose_name_plural = "Фото планов объектов"


class Offer(models.Model):
    title = models.CharField(
        'Название проекта',
        max_length=255,
    )

    price = models.PositiveBigIntegerField(
        'Цена',
    )

    house_area = models.FloatField(
        'Площадь дома (м²)',
    )

    territory_area = models.FloatField(
        'Площадь земли',
    )

    territory_area_points = models.CharField(
        'Единицы измерения площади земли',
        max_length=255,
        choices=(
            ('м²', 'м²'),
            ('км²', 'км²'),
            ('сот.', 'сот.'),
            ('а', 'а'),
            ('га', 'га'),
        ),
    )

    room_count = models.PositiveIntegerField(
        'Количество комнат',
    )

    floor_count = models.PositiveIntegerField(
        'Количество этажей',
    )

    exit_to_the_terrace = models.BooleanField(
        'Выход на террасу',
    )

    deadline = models.FloatField(
        'Сроки работ',
    )

    deadline_points = models.CharField(
        'Единицы измерения сроков работ',
        max_length=255,
        choices=(
            ('час', 'час'),
            ('часа', 'часа'),
            ('часов', 'часов'),
            ('день', 'день'),
            ('дня', 'дня'),
            ('дней', 'дней'),
            ('неделю', 'неделю'),
            ('недели', 'недели'),
            ('недель', 'недель'),
            ('месяц', 'месяц'),
            ('месяца', 'месяца'),
            ('месяцев', 'месяцев'),
            ('год', 'год'),
            ('года', 'года'),
            ('лет', 'лет'),
        ),
    )

    finishing = models.CharField(
        'Отделка',
        max_length=255,
        choices=(
            ("Черновая", "Черновая"),
            ("Предчистовая", "Предчистовая"),
            ("Чистовая", 'Чистовая'),
        ),
    )

    description = models.TextField(
        'Описание',
    )

    main_photo = models.ForeignKey(
        OfferPhotoMain,
        on_delete=models.SET_NULL,
        verbose_name='Главное фото',
        null=True,
    )

    photo = models.ManyToManyField(
        OfferPhoto,
        verbose_name='Фото',
        blank=True,
    )

    plan_photo = models.ManyToManyField(
        OfferPhotoPlan,
        verbose_name='План дома',
        blank=True,
    )

    address = models.CharField(
        "Полный адрес",
        max_length=255,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Предложение"
        verbose_name_plural = "Предложения"

    def get_price(self):
        return f'{self.price:,}'.replace(',', ' ') + " ₽"

    def get_house_area(self):
        return f"{self.house_area}  м²"

    def get_territory_area(self):
        return f"{self.territory_area} {self.territory_area_points}"

    def get_exit_to_the_terrace(self):
        return "Есть" if self.exit_to_the_terrace == True else "Нет"

    def get_deadline(self):
        return f"{self.deadline} {self.deadline_points}"

    def get_address(self):
        return self.address.replace(" ", '+') if self.address else "Казань"

    def image_preview(self):
        return mark_safe(
            '<img src="{url}"  style="width: 12vw; height: auto;" />'.format(
                url=self.main_photo.file.url,
                width=self.main_photo.file.width,
                height=self.main_photo.file.height,
            )
        )


class Request(models.Model):
    name = models.CharField(
        'Имя',
        max_length=255,
        null=True,
        blank=True,
    )
    phone = models.CharField(
        'Телефон',
        max_length=255,
        null=True,
        blank=True,
    )
    email = models.CharField(
        'Email',
        max_length=255,
        null=True,
        blank=True,
    )
    message = models.CharField(
        'Сообщение',
        max_length=255,
        null=True,
        blank=True,
    )
    time_created = models.DateTimeField(
        'Дата создания',
        editable=False,
        auto_now_add=True,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.name if self.name else ''} {self.phone if self.phone else ''} {self.email if self.email else ''}"

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"


class Review(models.Model):
    name = models.CharField(
        'Имя',
        max_length=255,
        blank=True,
        default='Аноним',
    )

    text = models.TextField(
        'Текст отзыва',
    )

    time_created = models.DateTimeField(
        'Дата создания',
        editable=False,
        auto_now_add=True,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.name}: {self.text[:15]}..."

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
