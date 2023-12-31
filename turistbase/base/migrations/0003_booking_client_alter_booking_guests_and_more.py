# Generated by Django 4.2.6 on 2023-11-06 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_booking_is_processed'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.client'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='guests',
            field=models.IntegerField(choices=[(1, '1 '), (2, '2 '), (3, '3 '), (4, '4 '), (5, '5 ')], verbose_name='Количество гостей'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='rooms',
            field=models.IntegerField(choices=[(1, '1 дом'), (2, '2 дома'), (3, '3 дома'), (4, '4 дома'), (5, '5 дом'), (6, '6 дом'), (7, '7 дом'), (8, '8 дом')], verbose_name='Количество домов'),
        ),
    ]
