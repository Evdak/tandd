from django.contrib import admin
from tgbot import models


@admin.register(models.TGUser)
class TGUserAdmin(admin.ModelAdmin):
    list_display = (

        'name',
        'tg_id',
        'is_admin',
    )

    list_filter = list_display
