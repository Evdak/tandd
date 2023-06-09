# Generated by Django 4.2 on 2023-04-17 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0005_offer_address'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='offerphoto',
            options={'verbose_name': 'Фото объектов', 'verbose_name_plural': 'Фото объектов'},
        ),
        migrations.AlterModelOptions(
            name='offerphotomain',
            options={'verbose_name': 'Фото объектов главные', 'verbose_name_plural': 'Фото объектов главные'},
        ),
        migrations.AlterModelOptions(
            name='offerphotoplan',
            options={'verbose_name': 'Фото планов объектов', 'verbose_name_plural': 'Фото планов объектов'},
        ),
        migrations.AlterField(
            model_name='offer',
            name='photo',
            field=models.ManyToManyField(blank=True, to='offers.offerphoto', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='plan_photo',
            field=models.ManyToManyField(blank=True, to='offers.offerphotoplan', verbose_name='План дома'),
        ),
    ]
