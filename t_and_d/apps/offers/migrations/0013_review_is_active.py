# Generated by Django 4.2 on 2023-05-14 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0012_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Отображать на сайте'),
        ),
    ]