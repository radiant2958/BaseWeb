# Generated by Django 4.2.4 on 2023-08-25 06:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Имя")),
                (
                    "phone",
                    models.CharField(max_length=15, verbose_name="Номер телефона"),
                ),
                ("date_in", models.DateField(verbose_name="Заезд")),
                ("date_out", models.DateField(verbose_name="Выезд")),
                (
                    "guests",
                    models.IntegerField(
                        choices=[(2, "2 гостя"), (3, "3 гостя"), (4, "4 гостя")],
                        verbose_name="Количество гостей",
                    ),
                ),
                (
                    "rooms",
                    models.IntegerField(
                        choices=[
                            (1, "1 дом"),
                            (2, "2 дома"),
                            (3, "3 дома"),
                            (4, "4 дома"),
                            (5, "5 дом"),
                            (6, "6 дом"),
                            (7, "7 дом"),
                        ],
                        verbose_name="Количество домов",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Имя")),
                (
                    "phone",
                    models.CharField(max_length=15, verbose_name="Номер телефона"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="News",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Заголовок")),
                ("content", models.TextField(verbose_name="Содержание")),
                (
                    "pub_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата публикации"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор",
                    ),
                ),
            ],
            options={
                "verbose_name": "Новость",
                "verbose_name_plural": "Новости",
            },
        ),
    ]
