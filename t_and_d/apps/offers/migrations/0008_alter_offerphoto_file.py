# Generated by Django 4.2 on 2023-04-18 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0007_alter_offerphotomain_file_alter_offerphotoplan_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offerphoto',
            name='file',
            field=models.ImageField(upload_to='offer_photo', verbose_name='Файл с фото'),
        ),
    ]