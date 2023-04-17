from django.contrib import admin
from offers import models


@admin.register(models.Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'price',
        'house_area',
        'territory_area',
        'territory_area_points',
        'room_count',
        'exit_to_the_terrace',
        'deadline',
        'deadline_points',
        'finishing',
        'description',
        'address',
    )

    list_filter = list_display


@admin.register(models.OfferPhoto)
class OfferPhotoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'file',
    )

    list_filter = list_display


@admin.register(models.OfferPhotoMain)
class OfferPhotoMainAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'file',
    )

    list_filter = list_display


@admin.register(models.OfferPhotoPlan)
class OfferPhotoPlanAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'file',
    )

    list_filter = list_display
