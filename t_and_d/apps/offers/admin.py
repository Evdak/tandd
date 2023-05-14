from django.utils.safestring import mark_safe
from django.contrib import admin
from offers import models
import jazzmin.templates


@admin.register(models.Offer)
class OfferAdmin(admin.ModelAdmin):
    list_filter = [
        "id",
        "title",
        "price",
        "house_area",
        "territory_area",
        "territory_area_points",
        "room_count",
        "exit_to_the_terrace",
        "deadline",
        "deadline_points",
        "finishing",
        "description",
        "address",
    ]

    list_display = [
        "image_preview",
        "id",
        "title",
        "get_price",
        "get_house_area",
        "get_territory_area",
        "room_count",
        "exit_to_the_terrace",
        "get_deadline",
        "finishing",
        "description",
        "address",
    ]

    def image_preview(self, obj: models.Offer):
        return obj.image_preview()

    def get_price(self, obj: models.Offer):
        return obj.get_price()

    def get_house_area(self, obj: models.Offer):
        return obj.get_house_area()

    def get_territory_area(self, obj: models.Offer):
        return obj.get_territory_area()

    def get_deadline(self, obj: models.Offer):
        return obj.get_deadline()

    image_preview.short_description = "Главное фото"
    get_price.short_description = "Цена"
    get_house_area.short_description = "Площадь дома"
    get_territory_area.short_description = "Площадь территории"
    get_deadline.short_description = "Сроки"

    class Media:
        css = {
            "all": ["css/offer_admin.css"],
        }
        js = ["js/offer_admin.js"]


@admin.register(models.OfferPhoto)
class OfferPhotoAdmin(admin.ModelAdmin):
    list_display = [
        "image_preview",
        "id",
        "file",
    ]

    list_filter = list_display.copy()[1:]

    def image_preview(self, obj: models.OfferPhoto):
        return obj.image_preview()


@admin.register(models.OfferPhotoMain)
class OfferPhotoMainAdmin(admin.ModelAdmin):
    list_display = [
        "image_preview",
        "id",
        "file",
    ]

    list_filter = list_display.copy()[1:]

    def image_preview(self, obj: models.OfferPhotoMain):
        return obj.image_preview()


@admin.register(models.OfferPhotoPlan)
class OfferPhotoPlanAdmin(admin.ModelAdmin):
    list_display = [
        "image_preview",
        "id",
        "file",
    ]

    list_filter = list_display.copy()[1:]

    def image_preview(self, obj: models.OfferPhotoPlan):
        return obj.image_preview()


@admin.register(models.Request)
class RequestAdmin(admin.ModelAdmin):
    ordering = ("-time_created",)

    list_display = [
        "id",
        "name",
        "phone",
        "email",
        "message",
        "time_created",
    ]

    list_filter = list_display.copy()


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    ordering = ("-time_created",)

    list_display = [
        "id",
        "name",
        "text",
        "is_active",
        "time_created",
    ]

    list_filter = list_display.copy()
